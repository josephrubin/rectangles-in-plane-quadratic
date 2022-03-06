# Rectangles in the Plane

An `O(n^2)` algorithm for counting the number of (not necessarily axis-aligned) rectangles formed from a set of points in the 2D plane (though this algorithm easily generalizes to finding rectangles among points of any dimension).

## Problem Statement

Given a list of `n` unique points in the 2D plane, return the total number of rectangles formed by the points.

From what I've seen, papers and articles always deal with finding squares or *axis-aligned* rectangles in `O(n^2)` time.

The following is the `O(n^2)` algorithm for finding the number of rectangles of any form in the 2D plane.

## Background

In *Programming Pearls* Jon Bentley proposes the problem of finding all anagram classes among a dictionary of words. One potential solution which is immediately discarded is comparing each word to each other word (because the goal here is a sub-quadratic solution). This would be like forming `n^2` line segments from our point set and comparing each segment to each other (an `O(n^4)` enterprise).

Then he says

> The *aha!* insight is to sign each word in the dictionary so that words in the same anagram class have the same *signature*, and then bring together words with equal signatures.

He further explains

> When an equivalence relation defines classes, it is helpful to define a signature such that every item in a class has the same signature and no other item does. Sorting the letters within a word yields one signature for an anagram class[.]

For our problem, we can imagine that he said

> The *aha!* insight is to sign each line segment so that those which form rectangles with each other have the same *signature*, and then bring together segments with equal signatures.

If you think about it, the *line one FORMS A RECTABLGE WITH line two* relation is transitive....

## Algorithm

There are O(n^2) total line segments. Each can be associated with all other lines it will form a rectangle with (that we've seen so far) in constant time if we find the appropriate signature (hash key).

Calculate the segment's length (`l`) along with the slope (`s`) and intercept (`i`) of the ray normal to its lower point (in some chosen orientation). Lines will form rectangles with each other if and only if these three parameters are equal. So consider `(l, s, i)` to be the hash key and increase our total rectangle count by the number of other lines we've seen so far with this key.

Horizonal lines are a special case: their normals have infinite slope so we use the `x` values of those normals as `i`.

## Code

Just take a look at `main.py` for the implementation.
```sh
$ . env/bin/activate
$ python main.py 
```
The above should run without producing any output (all tests pass).

## Higher Dimensions

If we have points in `R^N` the algorithm is mostly the same. We've signed each line segment by the two parameters of its normal ray (and the segment's length), but in general we can use the `N` parameters of the normal hyperplane incident to some chosen point on each line segment (such as the lower point or the midpoint). The rest of the algorithm is unchanged.
