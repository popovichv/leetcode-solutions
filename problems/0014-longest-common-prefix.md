# 14. Longest Common Prefix

**Difficulty:** `Easy`  
**Topics:** `String`

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string `""`.

## Explanation

Firstly, we find the shortest word in the array since the longest common prefix can only be
as long as the shortest word, and scanning by its length also guarantees that `s[i]` is a
valid index for every other word.

Then, using a vertical scanning approach, we compare each character starting from the beginning for every word.
We take `char = shortest_word[i]` and check it against character `i` of every word. As soon as at least one
character doesn't match, everything before `i` was common to all of them, so we return the slice of the shortest
word up until the current index.

If the loop finishes without a mismatch, the whole shortest word is the prefix, so we return it in the end.

## Code

Time complexity: `O(s*m)`, where `s` is the number of strings and `m` is the shortest length
Space complexity: `O(m)`

```python
# Python 3
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest_word = min(strs, key=len)

        for i in range(len(shortest_word)):
            char = shortest_word[i]

            for s in strs:
                if s[i] != char:
                    return shortest_word[:i]

        return shortest_word
```
