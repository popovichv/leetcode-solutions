# 1929. Concatenation of Array

**Difficulty:** `Easy`  
**Topics:** `Array`

Given an integer array `nums` of length `n`, you want to create an array `ans` of length `2n`
where `ans[i] == nums[i]` and `ans[i + n] == nums[i]`. Specifically, `ans` is the concatenation of two `nums` arrays.

## Explanation

### Loop Method

We create an array `ans` of size `2n` filled with zeros. Then, for each index `i` in `nums`,
we set `ans[i] = nums[i]` (first copy) and `ans[i + n] = nums[i]` (second copy). The second
copy begins `n` positions after the first, so `i + n` is always the right slot.

### Concatenation Method

We use built in list concatenation to return a new array, which contains of all elements of `nums`,
followed by the all elements of `nums` once again.

## Code

### Loop Method

Time complexity: `O(n)`  
Space complexity: `O(n)`

```python
# Python 3
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * (2 * n)

        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans
```

### Concatenation Method

Time complexity: `O(n)`  
Space complexity: `O(n)`

```python
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums
```
