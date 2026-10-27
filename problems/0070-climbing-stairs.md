# 70. Climbing Stairs

**Difficulty:** `Easy`  
**Topics:** `Dynamic Programming` `Memoization`

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

## Explanation

To reach step `n`, the last move was either a 1-step climb from step `n - 1` or a 2-step climb from step `n - 2`. So the number of ways to reach `n` is the sum of the ways to reach those two steps: `ways(n) = ways(n - 1) + ways(n - 2)`

A plain recursive solution recomputes the same values many times, which takes `O(2^n)` time. To avoid this, each result is stored in a dictionary the first time it is computed. Later calls read it from the cache, so every value from 3 to `n` is computed only once.

## Code

Time complexity: `O(n)`  
Space complexity: `O(n)`

```python
# Python 3
class Solution:
    calculated_steps = dict()

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if n not in self.calculated_steps:
            self.calculated_steps[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.calculated_steps[n]
```
