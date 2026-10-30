# 704. Binary Search

**Difficulty:** `Easy`  
**Topics:** `Array` `Binary Search`

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`.
If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

## Explanation

We keep two pointers, `low` and `high`, marking the part of the array that is still being searched. `mid` is the middle index between them, rounded down.

While `low <= high`:

- If `nums[mid] == target`, return `mid`.
- If `target > nums[mid]`, the target can only be to the right, so move `low` to `mid + 1`.
- Otherwise, the target can only be to the left, so move `high` to `mid - 1`.

We skip `mid` itself (`+ 1` / `- 1`) because it has already been checked. If the loop ends with `low > high`, the search range is empty and `target` is not in the array, so return `-1`.

## Code

Time complexity: `O(logn)`  
Space complexity: `O(1)`

```python
# Python 3
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0,  len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return -1
```
