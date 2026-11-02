# 232. Implement Queue Using Stacks

**Difficulty:** `Easy`  
**Topics:** `Stack` `Queue` `Design`

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

Implement the `MyQueue` class:

- `void push(int x)` Pushes element `x` to the back of the queue.
- `int pop()` Removes the element from the front of the queue and returns it.
- `int peek()` Returns the element at the front of the queue.
- `boolean empty()` Returns `true` if the queue is empty, `false` otherwise.

## Explanation

The two stacks have fixed roles:

- `s1` (input): every `push` goes here.
- `s2` (output): `pop` and `peek` read from here. Its top is always the front of the queue.

The `move` helper transfers elements from `s1` to `s2`, but only when `s2` is empty. If `s2` still has elements, they are older than anything in `s1`, so they must be served first. Moving early would break the order.

Example: push 1, 2, 3 gives `s1 = [1, 2, 3]`. On the first `pop`, `s2` is empty, so all elements move and `s2 = [3, 2, 1]`. Popping returns `1`, the oldest element. If we then push 4, it waits in `s1` until `s2` is used up.

Each element is moved from `s1` to `s2` at most once, so a single `pop`/`peek` can cost `O(n)`, but the cost averaged over all operations is `O(1)`.

## Code

Time complexity: `O(1)` - `O(n)`  
Space complexity: `O(n)`

```python
# Python 3
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []


    def push(self, x: int) -> None:
        self.s1.append(x)


    def move(self) -> None:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())


    def pop(self) -> int:
        self.move()
        return self.s2.pop()


    def peek(self) -> int:
        self.move()
        return self.s2[-1]


    def empty(self) -> bool:
        return not self.s1 and not self.s2
```
