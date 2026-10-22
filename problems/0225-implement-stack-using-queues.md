# 225. Implement Stack Using Queues

**Difficulty:** `Easy`  
**Topics:** `Stack` `Queue` `Design`

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `top`, `pop`, and `empty`).

Implement the `MyStack` class:

- `void push(int x)` Pushes element `x` to the top of the stack.
- `int pop()` Removes the element on the top of the stack and returns it.
- `int top()` Returns the element on the top of the stack.
- `boolean empty()` Returns `true` if the stack is empty, `false` otherwise.

## Explanation

We use two queues: `first_que` holds the stack, `second_que` is temporary storage.
The back of the queue is always the top of the stack.

A queue only lets us remove from the front, so the top (the last element added) is
reachable only after removing everything before it.

- **push:** append to the back of `first_que` and remember it in `top_item`. O(1).
- **top:** return `top_item`. O(1).
- **pop:**
  1. Move every element except the last from `first_que` to `second_que`.
     Each moved element is saved in `top_item`, so after the loop it holds the
     second-to-last element, which is the new top.
  2. Remove and return the last element from `first_que`.
  3. Swap the two queues' names. `second_que` now holds the remaining stack,
     and `first_que` is empty and ready for reuse. No copying back is needed.
     O(n).
- **empty:** check whether `first_que` is empty. O(1).

## Code

Time complexity: `O(1)` - `O(n)`  
Space complexity: `O(n)`

```python
# Python 3
class MyStack:

    def __init__(self):
        self.first_que = []
        self.second_que = []
        self.top_item = None

    def push(self, x: int) -> None:
        self.first_que.append(x)
        self.top_item = x

    def pop(self) -> int:
        while len(self.first_que) > 1:
            self.top_item = self.first_que.pop(0)
            self.second_que.append(self.top_item)

        item = self.first_que.pop(0)
        self.first_que, self.second_que = self.second_que, self.first_que
        return item

    def top(self) -> int:
        return self.top_item

    def empty(self) -> bool:
        return not self.first_que
```
