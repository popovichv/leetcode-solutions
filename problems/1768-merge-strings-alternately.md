# 1768. Merge Strings Alternately

**Difficulty:** `Easy`  
**Topics:** `String` `Two Pointers`

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

## Explanation

Both strings are read at the same pace, so a single index is enough instead of two pointers.

1. For each index up to the shorter length, append a letter from `word1`, then from `word2`.
2. Add whatever is left of the longer string after `min_len`.
3. Join the list into a string at the end.

## Code

Time complexity: `O(n + m)`  
Space complexity: `O(n + m)`

```python
# Python 3
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        min_len = min(len(word1), len(word2))

        for i in range(min_len):
            result.append(word1[i])
            result.append(word2[i])

        result.extend(word1[min_len:])
        result.extend(word2[min_len:])

        return "".join(result)
```
