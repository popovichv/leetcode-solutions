# 215. Kth Largest Element in an Array

**Difficulty:** `Medium`  
**Topics:** `Array` `Quickselect` `Dutch National Flag Algorithm`

Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array.

Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.

## Explanation

We use quickselect, which is based on quicksort, but after each partition we recurse into only the one part that
contains `target`. The pivot is chosen randomly so that sorted inputs don't push into the O(n^2) worst case.

For partition we use Dutch National Flag algorithm, which helps us to get rid of many elements at once in
case they are equal to pivot. We keep `low`, `mid` and `high` pointers.

For each `nums[mid]`:

- `nums[mid] < pivot`: swap `nums[low]` and `nums[mid]`, increment both. This moves smaller values to the left.
- `nums[mid] > pivot`: swap `nums[high]` and `nums[mid]`, decrement `high`. This moves larger values to the right.
  `mid` stays in place because the swapped-in element hasn't been checked yet.
- `nums[mid] == pivot`: increment `mid`. The value stays in the middle group.

After partitioning, every element in `[low, high]` equals the pivot. Then:

- If `target < low`, recurse on the left part `[s, low - 1]`.
- If `target > high`, recurse on the right part `[high + 1, e]`.
- Otherwise, `target` is inside the pivot group, so the pivot is the answer.

## Code

Time complexity: `O(n)` - `O(n^2)`  
Space complexity: `O(logn)`

```python
# Python 3
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        target = len(nums) - k
        return self.quickSelect(nums, 0, len(nums) - 1, target)


    def quickSelect(self, nums, s, e, target):
        pivot = nums[random.randint(s, e)]

        low, mid, high = s, s, e
        while mid <= high:
            if nums[mid] < pivot:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] > pivot:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
            else:
                mid += 1


        if target < low:
            return self.quickSelect(nums, s, low - 1, target)
        elif target > high:
            return self.quickSelect(nums, high + 1, e, target)
        else:
            return pivot
```
