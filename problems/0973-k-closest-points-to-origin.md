# 973. k Closest Points to Origin

**Difficulty:** `Medium`  
**Topics:** `Array` `Heap` `Quickselect`

Given an array of `points` where `points[i] = [x, y]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points on the X-Y plane is the Euclidean distance (i.e., `√(x1 - x2)^2 + (y1 - y2)^2`).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

## Explanation

### Heap Method

We keep a max-heap of size `k` holding the closest points we have seen so far. The root is the farthest of them, so it is the first one to drop when a closer point appears.

We compare squared distances (`x² + y²`) instead of real ones. Square root preserves order, so the result is the same, and we avoid float math.

For each point:

- Calculate its squared distance.
- If the heap has fewer than `k` elements, push the point.
- Otherwise, if the point is closer than the heap's maximum, replace the maximum with it.

After the loop, the heap contains exactly the `k` closest points.

### Quickselect Method

We only need to know which `k` points are closest, not their order. Quickselect partitions the array around a random pivot, like Quicksort, but recurses into one side only.

After partitioning, the pivot sits at index `w`: everything left of it is closer or equal, everything right is farther.

- `w == k - 1`: the first k elements are the answer. Stop.
- `w > k - 1`: search the left part.
- `w < k - 1`: search the right part.

A random pivot makes consistently bad splits unlikely, giving `O(n)` on average.

## Code

### Heap Method

Time complexity: `O(n*logk)`  
Space complexity: `O(k)`

```python
# Python 3
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distances = []
        for x, y in points:
            distance = x**2 + y**2

            if len(distances) < k:
                heappush_max(distances, (distance, x, y))
            elif distance < distances[0][0]:
                heapreplace_max(distances, (distance, x, y))

        return [[x, y] for d, x, y in distances]
```

### Quickselect Method

Time complexity: `O(n)` - `O(n^2)`  
Space complexity: `O(n)`

```python
# Python 3
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distances = []
        for x, y in points:
            distances.append((x**2 + y**2, x, y))

        results = self.quickSelect(distances, 0, len(distances) - 1, k - 1)
        return [[x, y] for dist, x, y in results[:k]]

    def quickSelect(self, distances, st, end, target):
        random_pivot = random.randint(st, end)
        distances[random_pivot], distances[end] = distances[end], distances[random_pivot]
        pivot = distances[end]

        w = st
        for i in range(st, end):
            if distances[i] <= pivot:
                distances[i], distances[w] = distances[w], distances[i]
                w += 1

        distances[w], distances[end] = distances[end], distances[w]

        if w == target:
            return distances
        elif w > target:
            return self.quickSelect(distances, st, w - 1, target)
        else:
            return self.quickSelect(distances, w + 1, end, target)
```
