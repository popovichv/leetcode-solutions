# 680. Valid Palindrome

**Difficulty:** `Easy`  
**Topics:** `Array` `Two Pointers` `Greedy`

Given a string `s`, return `true` if the `s` can be palindrome after deleting at most one character from it.

## Explanation

Use two pointers moving inward, as in a normal palindrome check. On the first mismatch, we must delete either `s[left]` or `s[right]`.
We can't pick greedily based on which neighbor matches, because both may match one step ahead while only one leads to a full palindrome.
So we check both remaining substrings (without any further deletions) and return `true` if either one is a palindrome.
If the pointers meet without a mismatch, the string is already a palindrome.

## Code

Time complexity: `O(n)`  
Space complexity: `O(1)`

```python
# Python 3
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False

                i += 1
                j -= 1

            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)

            left += 1
            right -= 1

        return True
```
