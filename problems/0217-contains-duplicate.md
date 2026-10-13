# 217. Contains Duplicate

## Explanation

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

---

### Sorting Method

Brute force checks every pair in `O(n^2)`. Instead, we sort the array first.
After sorting, duplicate values are adjucent, so we only compare each element
with its neigbour. If any two neighbours are equal, return True.

### HashSet Method

A set stores only unique values. If we convert the array to a set and its length
is not equal (or smaller) than the original array's length, at least one value appeared more
than once, so we return True.

## Code

### Sorting Method

Time complexity: `O(n*logn)`  
Space complexity: `O(n)`

```python
# Python 3
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()

        for i in range(len(nums) - 1):
            if (nums[i] == nums[i + 1]):
                return True

        return False
```

### HashSet Method

Time complexity: `O(n)`  
Space complexity: `O(n)`

```python
# Python 3
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)
```
