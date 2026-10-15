# 27. Remove Duplicates

**Difficulty:** `Easy`  
**Topics:** `Array` `Two Pointers`

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place.
The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.
Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted

## Explanation

Use two pointers: `left` scans from the start, `right` marks the last unchecked element.

- If `nums[left] == val`, swap it with `nums[right]` and move `right` one step left.
  Do not move `left`, since the swapped-in element has not been checked yet.
- Otherwise, the element is kept: move `left` forward and increase `k`.

Stop when `left > right`. `k` is the number of elements that are not equal to `val`.

## Code

Time complexity: `O(n)`  
Space complexity: `O(1)`

```python
# Python 3
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0

        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
                k += 1

        return k
```
