# 78. Subsets

**Difficulty:** `Medium`  
**Topics:** `Array` `Backtracking`

Given an integer array `nums` of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

## Explanation

Each element has two choices: it's either in the subset or it isn't. That gives `2^n` subsets, and they form a decision tree.

DFS goes through `nums` one index at a time and branches at each step:

- Take: continue with `path + [nums[i]]`.
- Skip: continue with `path` unchanged.

When `i == len(nums)`, every element has been decided, so `path` is a complete subset and gets added to `result`.

## Code

Time complexity: `O(n*2^n)`  
Space complexity: `O(n)`

```python
# Python 3
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def branch(i, path):
            if i == len(nums):
                result.append(path)
                return

            branch(i + 1, path + [nums[i]])
            branch(i + 1, path)

        branch(0, [])
        return result
```
