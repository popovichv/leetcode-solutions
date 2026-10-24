# 125. Valid Palindrome

**Difficulty:** `Easy`  
**Topics:** `Two Pointers` `String`

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Explanation

First clean the string: remove all non-alphanumeric characters and convert it to lowercase.
Then use two pointers, one at each end, and compare the characters they point to. If any pair differs,
it is not a palindrome. If the pointers meet without a mismatch, it is. The loop stops when `left >= right`,
since the middle character always matches itself.

## Code

Time complexity: `O(n)`  
Space complexity: `O(n)`

```python
# Python 3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
```
