# 155. Min Stack

**Difficulty:** `Medium`  
**Topics:** `Stack`

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

- `MinStack()` initializes the stack object.
- `void push(int value)` pushes the element value onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

## Explanation

This problem is a trivial stack implementation, except for `int getMin()` function.

In order to return the minimum value in constant time, it has to be stored with each element in the stack - it becomes a pair.
Each entry stores the smaller of its own value and the minimum of everything below it, which is essentialy a "minimum so far",
meaning each entry stores the minimum up until itself, so when newer elements with potential lower minimum are popped out,
actual minimum for the current stack condition is still available.

## Code

Time complexity: `O(1)`  
Space complexity: `O(n)`

```python
# Python 3
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        if self.stack:
            min_val = min(self.stack[-1][1], value)
        else:
            min_val = value

        self.stack.append([value, min_val])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
```
