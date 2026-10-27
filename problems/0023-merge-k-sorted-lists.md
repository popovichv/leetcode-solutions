# 23. Merge K Sorted Lists

**Difficulty:** `Hard`  
**Topics:** `Linked List` `Heap`

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

## Explanation

We add heads of linked lists to the priority queue as a tuple: `(priority, list_index, node)`.
The list index is a tie breaker, if two priority values are equal, python will use the index to determine position.

While the heap is not empty:

1. Pop the smallest node and append it to the tail of the result list.
2. If that node has a `next`, push `node.next` into the heap.

## Code

Time complexity: `O(n*logk)`  
Space complexity: `O(k)`

```python
# Python 3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = tail = ListNode()
        while heap:
            val, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
```
