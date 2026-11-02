# 347. Top K Frequent Elements

**Difficulty:** `Medium`  
**Topics:** `Array` `Hash Map` `Sorting` `Quickselect`

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

## Explanation

### Quick Select Method

We count occurrences of each element in a hash map, then convert it to a list of `(num, freq)` pairs.
Using quickselect, we partition the list around a random pivot frequency so that pairs with higher frequencies move to the left.
After each partition, the pivot is in its final sorted position. If it lands at index `k - 1`, the first `k` pairs are
the most frequent, so we return them. Otherwise, we recurse only into the side that contains index `k - 1`.

## Code

### Quick Select Method

Time complexity: `O(n)` - `O(n^2)`
Space complexity: `O(n)`

```python
# Python 3
class Solution:
    class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        map = defaultdict(int)
        for x in nums:
            map[x] += 1

        results = self.quickSelect(list(map.items()), 0, len(map) - 1, k - 1)
        return [key for key, value in results]

    def quickSelect(self, arr, start, end, target):
        pivot_index = random.randint(start, end)
        arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
        pivot = arr[end][1]

        w = start
        for i in range(start, end):
            if arr[i][1] > pivot:
                arr[i], arr[w] = arr[w], arr[i]
                w += 1

        arr[w], arr[end] = arr[end], arr[w]
        if w == target:
            return arr[:w + 1]
        elif w < target:
            return self.quickSelect(arr, w + 1, end, target)
        else:
            return self.quickSelect(arr, start, w - 1, target)
```
