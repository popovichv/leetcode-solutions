# 242. Valid Anagram

## Explanation

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

---

If the length of the strings differ, they cannot be anagrams, so we return `false`.
We count how many times each character occurs in both strings using two hashmaps. If the hashmaps are equal,
every character occurs the same number of times in both strings, so we return `true`. Otherwise, we return `false`.

## Code

Time complexity: `O(n)`  
Space complexity: `O(n)`

```python
# Python 3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        scount = defaultdict(int)
        tcount = defaultdict(int)

        for i in range(len(s)):
            scount[s[i]] += 1
            tcount[t[i]] += 1

        return scount == tcount
```
