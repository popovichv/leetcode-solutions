# 21. Merge Two Sorted Lists

**Difficulty:** `Easy`  
**Topics:** `Linked List`

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

## Explanation

We create a `dummy` node to keep track of the head by attaching the first node to `dummy.next`.

While there are nodes in both linked lists:

- If `list1.val > list2.val`, attach `list2` to `cur.next` and advance `list2`
- Otherwise, attach `list1` to `cur.next` and advance `list1`
- Move `cur` forward to the node we just attached

If one of the lists is empty, attach all elements from the other list to the end.
Return `dummy.next`, which is the first element we attached.

## Code

Time complexity: `O(n+m)`  
Space complexity: `O(1)`

```python
# Python 3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next

            cur = cur.next

        if list1 or list2:
            cur.next = list1 or list2

        return dummy.next
```
