"""An O(n^2) algorithm for counting the number of rectangles in a plane.

This algorithm avoids computational error by taking only integral coordinates
but in principal should be able to handle any points.
"""
import collections
import itertools
import random


Vector = collections.namedtuple('Vector', ['x', 'y'])


def count_rectangles(points):
  rectangle_count = 0
  line_classes = collections.defaultdict(list)

  for a, b in itertools.combinations(points, 2):
    # Ensure a is the lower point.
    if b.y < a.y:
      a, b = b, a
    # Or the leftmost point if horizontal.
    elif b.y == a.y and b.x < a.x:
      a, b = b, a

    line_vector = Vector(b.x - a.x, b.y - a.y)
    length = line_vector.x * line_vector.x + line_vector.y * line_vector.y

    # Compute the parameters of the ray normal to a.
    normal = Vector(line_vector.y, -line_vector.x)
    normal_slope = (normal.y, normal.x)

    if normal_slope[1] == 0:
      normal_intercept = None
    else:
      # norm_intercept is (a.y - a.x * (norm_slope[0] / norm_slope[1]))
      # so let's calculate this with ratios.
      denominator = normal_slope[1]
      numerator = a.y * denominator - a.x * normal_slope[0]
      normal_intercept = (numerator, denominator)

    # Form a hash key from the (length, normal_slope, normal_intercept) triplet.
    # One option (which we use) is to reduce each fraction to a certain precision.
    precision = 4
    key = (
      round(length, precision),
      round(normal_slope[0] / normal_slope[1], precision) if normal_slope[1] else None,
      round(normal_intercept[0] / normal_intercept[1], precision) if normal_intercept else (a.x, 1)
    )

    rectangle_count += len(line_classes[key])
    line_classes[key].append((a, b))

  return rectangle_count // 2


def run_tests():
  def p(x, y):
    return Vector(int(x), int(y))

  # Answers calculated by hand in Desmos.
  tests = [
    ([p(2, 1), p(2, 5), p(5, 5), p(5, 1)], 1),
    ([p(5, 2), p(8, 2), p(8, 7), p(5, 7), p(2, 1), p(2, 5), p(5, 5), p(5, 1)], 2),
    ([p(0, 0), p(0, 2), p(5, 0), p(5, 2), p(8, 2), p(8, 0), p(8, 7), p(5, 7), p(2, 1), p(2, 5), p(5, 5), p(5, 1)], 6),
    ([p(2, 5), p(5, 7), p(5, 0), p(8, 2)], 0),
    ([p(0, 0), p(-2, 4), p(2, 6), p(4, 2), p(-2, -2), p(-6, -6), p(-8, -4), p(-4, 0), p(2, -2), p(0, -4), p(6, 0)], 3),
    ([p(0, 0), p(-2, 4), p(2, 6), p(4, 2), p(-2, -2), p(-6, -6), p(-8, -4), p(-4, 0), p(2, -2), p(0, -4), p(6, 0), p(1, -2), p(5, 0)], 5)
  ]

  # Run each test with random ordering of the points.
  for i, (points, answer) in enumerate(tests):
    determined_random = random.Random(100)
    for ii in range(40):
      determined_random.shuffle(points)
      result = count_rectangles(points)
      if result != answer:
        print(f'Failure of test {i}.{ii}: expected {answer}; got {result}.')


if __name__ == '__main__':
  run_tests()
