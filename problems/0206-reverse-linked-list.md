# 206. Reverse Linked List

**Difficulty:** `Easy`  
**Topics:** `Linked List`

Given the `head` of a singly linked list, reverse the list, and return the reversed list.

## Explanation

We always keep two nodes - `prev` and `cur`.

While `cur` is not `None`:

- Save `cur.next` in `next_node`, so we don't lose the rest of the list.
- Point `cur.next` backwards, to `prev`.
- Move forward: `prev` becomes `cur`, and `cur` becomes `next_node`.

When the loop ends, `cur` is `None` and `prev` is the last node of the original
list. That node is the new head, so we return `prev`.

## Code

Time complexity: `O(n)`  
Space complexity: `O(1)`

```python
# Python 3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        cur = head

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        return prev
```
