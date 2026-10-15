# 485. Max Consecutive Ones

**Difficulty:** `Easy`  
**Topics:** `Array`

Given a binary array `nums`, return the maximum number of consecutive `1`'s in the array.

## Explanation

Iterate through the array while tracking `current`, the length of the current run of `1`s. On a `1`, increment `current` and update `max_consecutive` if `current` is larger. On a `0`, reset `current` to `0`.

## Code

Time complexity: `O(n)`
Space complexity: `O(1)`

```python
# Python 3
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        current = 0
        max_consecutive = 0

        for n in nums:
            if n == 1:
                current += 1
                max_consecutive = max(current, max_consecutive)
            else:
                current = 0

        return max_consecutive
```
