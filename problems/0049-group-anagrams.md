# 49. Group Anagrams

**Difficulty:** `Medium`  
**Topics:** `String` `Hash Table` `Array` `Sorting`

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

## Explanation

Create a hashmap that defaults to an empty array for new keys.

For each string:

- Sort the string alphabetically.
- Append the original string to the list stored under that key.

Return the hashmap’s values.

## Code

Time complexity: `O(n*k*logk)`  
Space complexity: `O(n*k)`

```python
# Python 3
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)

        for s in strs:
            groups["".join(sorted(s))].append(s)

        return list(groups.values())
```
