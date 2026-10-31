# 875. Koko Eating Bananas

**Difficulty:** `Medium`  
**Topics:** `Array` `Binary Search`

Koko loves to eat bananas. There are `n` piles of bananas, the `i`th pile has `piles[i]` bananas.
The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile.
If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

## Explanation

We keep two pointers, `low` and `high`, starting at `1` and `max(piles)`. `mid` is the middle number between them, rounded down.
`guess(piles, h, k)` calculates how many hours it will take to eat each pile with `k` speed. If in the end `h < 0`, `k` is too slow,
so we return `False`, otherwise `True.`

While `low <= high`:

- If `guess(mid)` is `True`, our guess is correct but might be high, so we save new lowest `k` and move `high` to `mid - 1`
- If `guess(mid)` is `False`, our guess is too low. Move `low` to `mid + 1`

## Code

Time complexity: `O(n*logm)`  
Space complexity: `O(1)`

```python
# Python 3
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        k = max(piles)

        low, high = 1, k
        while low <= high:
            mid = (low + high) // 2

            if self.guess(piles, h, mid):
                high = mid - 1
                k = mid
            else:
                low = mid + 1

        return k


    def guess(self, piles, h, k):
        for pile in piles:
            h -= math.ceil(pile / k)

        return h >= 0
```
