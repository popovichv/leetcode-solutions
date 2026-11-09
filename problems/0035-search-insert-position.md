# 35. Search Insert Position

**Difficulty:** `Easy`  
**Topics:** `Array` `Binary Search`

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

## Explanation

We use binary search, narrowing the range `[left, right]` by half on each step:

- If `nums[mid] < target`, the answer is to the right, so `left = mid + 1`.
- If `nums[mid] > target`, the answer is to the left, so `right = mid - 1`.
- If they are equal, we return `mid`.

Every element before `left` is smaller than `target`, and every element after `right` is larger. If the target is not found, the loop ends with `left = right + 1`, so `left` is the first index whose value is greater than `target`. That is the insertion position.

## Code

Time complexity: `O(logn)`  
Space complexity: `O(1)`

```python
# Python 3
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return left
```
