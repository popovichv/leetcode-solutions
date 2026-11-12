# 26. Remove Duplicates from Sorted Array

**Difficulty:** `Easy`  
**Topics:** `Array` `Two Pointers`

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in `nums` to be `k`​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements `k`.

The first `k` elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index `k - 1` can be ignored.

## Explanation

We use two pointers: `cur` iterates through the array, and `w` marks the position of the last written unique element.
The first element is always unique, so it counts as already written and `cur` starts at `1`.
Since the array is sorted, duplicates are adjacent. If `nums[cur]` differs from `nums[w]`, we've found a new unique value,
so we move `w` forward and write `nums[cur]` there. At the end, `w + 1` is the number of unique elements.

## Code

Time complexity: `O(n)`  
Space complexity: `O(1)`

```python
# Python 3
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        cur, w = 0, 0

        while cur < len(nums):
            if nums[w] != nums[cur]:
                w += 1
                nums[w] = nums[cur]

            cur += 1

        return w + 1
```
