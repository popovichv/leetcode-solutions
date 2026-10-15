# 1299. Replace Elements with Greatest Element on Right Side

**Difficulty:** `Easy`  
**Topics:** `Array`

Given an array `arr`, replace every element in that array with the greatest element among the elements to its right, and replace the last element with `-1`.

## Explanation

Traverse the array from right to left, keeping `max_val`: the greatest element seen so far to the right of the current position.

For each element:

1. Save its original value.
2. Overwrite it with `max_val`.
3. Update `max_val` if the original value is greater.

## Code

Time complexity: `O(n)`  
Space complexity: `O(1)`

```python
# Python 3
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        max_val = arr[-1]

        for i in range(len(arr) - 1, -1, -1):
            val = arr[i]
            arr[i] = max_val
            max_val = max(max_val, val)

        arr[-1] = -1
        return arr
```
