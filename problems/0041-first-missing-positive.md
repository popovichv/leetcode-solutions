# 41. First Missing Positive

**Difficulty:** `Hard`  
**Topics:** `Array` `Hash Table`

Given an unsorted integer array `nums`. Return the smallest positive integer that is not present in `nums`.

## Explanation

The answer is always in the range `1..n+1`, so the array itself can be used as a "seen" table: index `i` represents the number `i + 1`, and a negative sign means "seen".

1. Clean up: replace every number `<= 0` with `n + 1`, so all values are positive and the sign is free to use as a flag.
2. Mark: for each value `x = abs(nums[i])` in `1..n`, make `nums[x - 1]` negative. Use `-abs(...)` so duplicates don't flip the sign back.
3. Find: the first index `i` with a positive value means `i + 1` was never seen. If every value is negative, the answer is `n + 1`.

## Code

Time complexity: `O(n)`  
Space complexity: `O(1)`

```python
# Python 3
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            num = abs(nums[i])
            if 1 <= num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1
```
