# 1046. Last Stone Weight

**Difficulty:** `Easy`
**Topics:** `Array` `Heap`

You are given an array of integers `stones` where `stones[i]` is the weight of the `ith` stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`. The result of this smash is:

If `x == y`, both stones are destroyed, and
If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

## Explanation

We always need the two heaviest stones, so a max-heap is a good fit. It gives us the largest element in `O(log n)`.

1. Turn `stones` into a max-heap in place with `heapify_max`.
2. While at least two stones remain, pop the two heaviest (`first >= second`).
3. If they differ, push the remainder `first - second` back into the heap. If they are equal, both are destroyed and nothing is pushed.
4. When the loop ends there is either one stone left (return it) or none (return `0`).

## Code

Time complexity: `O(n*logn)`  
Space complexity: `O(1)`

```python
# Python 3
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heapify_max(stones)

        while len(stones) > 1:
            first, second = heappop_max(stones), heappop_max(stones)

            if first != second:
                heappush_max(stones, abs(first - second))

        return stones[0] if stones else 0
```
