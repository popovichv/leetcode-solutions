# 1472. Design Browser History

**Difficulty:** `Medium`  
**Topics:** `Linked List` `Design`

You have a browser of one tab where you start on the `homepage` and you can visit another `url`, get back in the history number of `steps` or move forward in the history number of `steps`.

Implement the `BrowserHistory` class:

- `BrowserHistory(string homepage)` Initializes the object with the `homepage` of the browser.
- `void visit(string url)` Visits `url` from the current page. It clears up all the forward history.
- `string back(int steps)` Move `steps` back in history. If you can only return `x` steps in the history and `steps > x`, you will return only `x` steps. Return the current `url` after moving back in history at most `steps`.
- `string forward(int steps)` Move `steps` forward in history. If you can only forward `x` steps in the history and `steps > x`, you will forward only `x` steps. Return the current `url` after forwarding in history at most `steps`.

## Explanation

We implement the history as a doubly linked list that tracks one pointer: current.

- Each node stores a URL, a pointer to the next tab, and a pointer to the previous tab.
- `current` marks the page we are on.
- `visit` attaches the new node after `current` and overwrites `current.next`. This drops all forward history at once, because the old nodes become unreachable.
- `back` and `forward` stop early when there is no `prev` or `next`, so we never move past either end.

## Code

Time complexity: `O(1)` - `O(n)`  
Space complexity: `O(n)`

```python
# Python 3
class BrowserTab:

    def __init__(self, url=None, prev=None, next=None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = BrowserTab(homepage)
        self.current = self.homepage

    def visit(self, url: str) -> None:
        new_tab = BrowserTab(url, self.current)
        self.current.next = new_tab
        self.current = new_tab

    def back(self, steps: int) -> str:
        while self.current.prev and steps > 0:
            steps -= 1
            self.current = self.current.prev

        return self.current.url

    def forward(self, steps: int) -> str:
        while self.current.next and steps > 0:
            steps -= 1
            self.current = self.current.next

        return self.current.url
```
