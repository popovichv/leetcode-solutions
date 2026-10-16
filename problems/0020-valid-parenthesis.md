# 20. Valid Parenthesis

**Difficulty:** `Easy`  
**Topics:** `String` `Stack`

Given a string s containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

## Explanation

First, we create a hashmap which maps every opening bracket to its corresponding closing bracket.

For each character `ch` in `s`:

- If the stack is empty, push `ch`.
- Otherwise, let `prev` be the top of the stack. If `prev` is an opening bracket
  and `ch` is its matching closing bracket, pop `prev`.
- Otherwise, push `ch`.

The string is valid if the stack is empty at the end.

## Code

Time complexity: `O(n)`  
Space complexity: `O(n)`

```python
# Python 3
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_brackets = {"(":")", "{":"}", "[":"]"}

        for ch in s:
            if not stack:
                stack.append(ch)
                continue

            prev = stack[-1]
            if prev in valid_brackets and ch == valid_brackets[prev]:
                stack.pop()
            else:
                stack.append(ch)

        return stack == []
```
