# 1. Two Sum

## Explanation

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. Each input has exactly one solution. You can return the answer in any order.

---

Brute force checks every pair in `O(n^2)`. Instead, we use a hashmap
(`checked_nums`) that maps each number we have seen to its index.

For each number:

- Calculate the complement (`target` - `num`)
- If the complement is not present in `checked_nums`, add the num as the key, and its index as the value
- If the complement is present in `checked_nums`, return its index with the current index

The complement we calculate is a second number that we need to add up to the current number to reach the target. By saving each previous number in a hashmap, we can efficiently check if there was a suitable pair for the current number before.

## Code

Time complexity: `O(n)`  
Space complexity: `O(n)`

```python
# Python 3
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        checked_nums = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in checked_nums:
                return [checked_nums[complement], i]

            checked_nums[num] = i
```
