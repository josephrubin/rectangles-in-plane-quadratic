# Rectangles in the Plane

An O(n^2) algorithm for counting the number of (not necessarily axis-aligned) rectangles formed from a set of points in the 2D plane.

From what I've seen, papers and articles always deal with finding squares or axis-aligned rectangles in O(n^2) time (sometimes in higher dimensions).

The following is the algorithm for finding the number of rectangles of any form in the 2D plane.

## Algorithm

There are O(n^2) total line segments. Each can be associated with all other lines it will form a rectangle with (that we've seen so far) in constant time.

To do so, calculate the segment's length along with the slope and intercept of the ray normal to its lower point. Lines will form rectangles with each other if and only if these three parameters are equal.

Horizonal lines are a special case - their normals have infinite slope so we use the x values of those normals as the intercept.

## Code

Just take a look at `main.py` for the implementation.
```sh
$ . env/bin/activate
$ python main.py 
```
The above should run without producing any output (all tests pass).
