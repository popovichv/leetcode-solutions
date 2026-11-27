# 150. Evaluate Reverse Polish Notation

**Difficulty:** `Medium`  
**Topics:** `Array` `Math` `Stack`

You are given an array of strings `tokens` that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

## Explanation

Use a stack to hold numbers. Push each number onto it until you reach an operator. Then pop the top two numbers, apply the operator, and push the result back. The second number popped is the left operand. When all tokens are processed, the one number left on the stack is the result.

## Code

Time complexity: `O(n)`  
Space complexity: `O(n)`

```python
# Python 3
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        numbers = []
        signs = {"+", "-", "*", "/"}

        for t in tokens:
            if t not in signs:
                numbers.append(int(t))
            else:
                n1 = numbers.pop()
                n2 = numbers.pop()

                if t == "+":
                    numbers.append(n2 + n1)
                elif t == "-":
                    numbers.append(n2 - n1)
                elif t == "*":
                    numbers.append(n2 * n1)
                else:
                    numbers.append(int(n2 / n1))

        return numbers[0]
```
