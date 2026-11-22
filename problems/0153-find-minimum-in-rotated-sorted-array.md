# 153. Find Minimum in Rotated Sorted Array

**Difficulty:** `Medium`  
**Topics:** `Array` `Binary Search`

Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.

## Explanation

A rotated sorted array is made of two sorted parts: a left part with the larger values and a right part with the smaller values. The minimum is the first element of the right part, right after the only "drop" in the array (where `nums[i] > nums[i+1]`).

Use binary search to find that drop, comparing with `nums[-1]` to tell which part `mid` is in:

- If `nums[mid] > nums[mid+1]`, `mid` is right before the drop, so `nums[mid+1]` is the minimum.
- If `nums[mid] > nums[-1]`, `mid` is in the left part, so the minimum is after it: `left = mid + 1`.
- Otherwise, `mid` is in the right part and could be the minimum itself, so keep it in range: `right = mid`.

If the loop ends without finding a drop, the array was never rotated, so the minimum is `nums[0]`.

## Code

Time complexity: `O(logn)`  
Space complexity: `O(1)`

```python
# Python 3
class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid+1]:
                return nums[mid + 1]
            elif nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid

        return nums[0]
```
