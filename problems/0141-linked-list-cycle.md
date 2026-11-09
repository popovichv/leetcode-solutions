# 141. Linked List Cycle

**Difficulty:** `Easy`  
**Topics:** `Linked List` `Floyd's Cycle Finding Algorithm`

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. Note that `pos` is not passed as a parameter.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

## Explanation

We use Floyd's cycle detection algorithm (tortoise and hare) with two pointers: `slow` moves one step at a time, and `fast` moves two steps.

- No cycle: `fast` reaches the end of the list (`fast` or `fast.next` is `None`), so we return `False`. Since `fast` is always ahead, it is the only pointer we need to check.
- Cycle: `fast` never reaches the end. Once both pointers are inside the cycle, the gap between them shrinks by one node each step, so `fast` eventually catches up with `slow`. When both point to the same node, we return `True`.

## Code

Time complexity: `O(n)`  
Space complexity: `O(1)`

```python
# Python 3
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False
```
