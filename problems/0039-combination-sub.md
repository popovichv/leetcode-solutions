# 39. Combination Sum

**Difficulty:** `Medium`
**Topics:** `Array` `Backtracking`

Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.

The same number may be chosen from `candidates` an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

## Explanation

Use backtracking to build combinations one number at a time, tracking how much of the target is still `remaining`.

- If `remaining < 0`, the path overshot the target, so stop.
- If `remaining == 0`, the path is a valid combination, so save it.
- Otherwise, try adding each candidate and recurse with `remaining` reduced by that candidate.

Without extra care, the same combination is generated in every order (`[2,2,3]`, `[2,3,2]`, `[3,2,2]`). To prevent this, pass a `start` index and only pick candidates from `start` onward. Recursing with `i` allows the same number to be reused, but the path can never go back to an earlier candidate. This means every combination is built in exactly one order (by index).

## Code

Time complexity: `O(n^(T/M + 1))`  
Space complexity: `O((T/M)^2)`

Where `n` is the number of candidates, `T` is the target, and `M` is the smallest candidate. The recursion depth is at most `T/M`, and each call loops over up to `n` candidates. Space comes from the recursion stack (`T/M` deep), where each frame holds its own copy of `path` (up to `T/M` long).

```python
# Python 3
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def combination(start, path, remaining):
            if remaining < 0:
                return

            if remaining == 0:
                result.append(path)
                return

            for i in range(start, len(candidates)):
                combination(i, path + [candidates[i]], remaining - candidates[i])

        combination(0, [], target)
        return result
```
