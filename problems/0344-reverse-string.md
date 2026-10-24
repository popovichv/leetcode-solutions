# 344. Reverse String

**Difficulty:** `Easy`  
**Topics:** `Two Pointers` `String`

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array in-place with `O(1)` extra memory.

## Explanation

Since we cannot allocate a new array, we modify the existing one in place.
Use two pointers, one at each end, and swap the elements they point to. Move both pointers
toward the center until they meet. The loop stops when `left >= right`, so the middle element
of an odd-length array stays where it is.

## Code

Time complexity: `O(n)`  
Space complexity: `O(1)`

```python
# Python 3
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
```
