# 125. Valid Palindrome

**Difficulty:** `Easy`  
**Topics:** `Two Pointers` `String`

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Explanation

### Regex Method

First clean the string: remove all non-alphanumeric characters and convert it to lowercase.
Then use two pointers, one at each end, and compare the characters they point to. If any pair differs,
it is not a palindrome. If the pointers meet without a mismatch, it is. The loop stops when `left >= right`,
since the middle character always matches itself.

### Skipping Method

The approach is similar to the regex method, the difference is how we skip non-alphanumeric characters from the
string. Inside the main loop we have two more loops for left and right pointer. If a character is not alphanumeric,
then we move the pointer inward. We do so until we encounter valid characters for both pointers, then proceed to comparison.

## Code

### Regex Method

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

### Skipping Method

Time complexity: `O(n)`  
Space complexity: `O(1)`

```python
# Python 3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
```
