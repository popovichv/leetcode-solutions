# 374. Guess Number Higher or Lower

**Difficulty:** `Easy`  
**Topics:** `Binary Search`

I pick a number from `1` to `n`. You have to guess which number I picked (the number I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API `int guess(int num)`, which returns three possible results:

`-1`: Your guess is higher than the number I picked (i.e. `num > pick`).
`1`: Your guess is lower than the number I picked (i.e. `num < pick`).
`0`: your guess is equal to the number I picked (i.e. `num == pick`).

Return the number that I picked.

## Explanation

We keep two pointers, `low` and `high`, starting at `1` and `n`. `mid` is the middle number between them, rounded down.

While `low <= high`:

- If `guess(mid) == 1`, our guess is too low, so the pick is to the right. Move `low` to `mid + 1`.
- If `guess(mid) == -1`, our guess is too high, so the pick is to the left. Move `high` to `mid - 1`.
- If `guess(mid) == 0`, we found it. Return `mid`.

## Code

Time complexity: `O(logn)`  
Space complexity: `O(1)`

```python
# Python 3
class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n

        while low <= high:
            mid = (low + high) // 2

            if guess(mid) > 0:
                low = mid + 1
            elif guess(mid) < 0:
                high = mid - 1
            else:
                return mid
```
