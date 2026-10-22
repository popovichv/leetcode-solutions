# 206. Reverse Linked List

**Difficulty:** `Easy`  
**Topics:** `Linked List` `Recursion`

Given the `head` of a singly linked list, reverse the list, and return the reversed list.

## Explanation

### Recursive Method

Assume `reverseList(head.next)` already reverses the rest of the list and returns its new head.

- Base case: an empty list or a single node is already reversed, so return `head`. For the last node of the original list, this becomes the new head of the whole list.
- Recurse: call `reverseList(head.next)`. Everything after `head` is now reversed, but `head.next` still points to the old second node, which is now the tail of the reversed part.
- Attach: `head.next.next = head` makes that tail point back to `head`.
- Cut: `head.next = None`, because `head` is now the tail. Without this, we get a cycle.
- Return `new_head` unchanged. It is the same node on every level of the call stack.

### Iterative Method

We always keep two nodes - `prev` and `cur`.

While `cur` is not `None`:

- Save `cur.next` in `next_node`, so we don't lose the rest of the list.
- Point `cur.next` backwards, to `prev`.
- Move forward: `prev` becomes `cur`, and `cur` becomes `next_node`.

When the loop ends, `cur` is `None` and `prev` is the last node of the original
list. That node is the new head, so we return `prev`.

## Code

### Recursive Method

Time complexity: `O(n)`  
Space complexity: `O(n)`

```python
# Python 3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head
```

### Iterative Method

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
