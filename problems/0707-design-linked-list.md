# 707. Design Linked List

**Difficulty:** `Medium`  
**Topics:** `Linked List` `Design`

Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: `val` and `next`. `val` is the value of the current node,
and `next` is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more
attribute `prev` to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the `MyLinkedList` class:

- `MyLinkedList()` Initializes the `MyLinkedList` object.
- `int get(int index)` Get the value of the `index`th node in the linked list. If the index is invalid, return `-1`.
- `void addAtHead(int val)` Add a node of value `val` before the first element of the linked list. After the insertion,
  the new node will be the first node of the linked list.
- `void addAtTail(int val)` Append a node of value `val` as the last element of the linked list.
- `void addAtIndex(int index, int val)` Add a node of value `val` before the `index`th node in the linked list. If `index` equals
  the length of the linked list, the node will be appended to the end of the linked list. If `index` is greater than the length,
  the node will not be inserted.
- `void deleteAtIndex(int index)` Delete the `index`th node in the linked list, if the `index` is valid.

## Explanation

We implement the list as a doubly linked list that tracks three things: a `head` pointer, a `tail` pointer, and a `size` counter.

- Each node stores a value, a pointer to the next node, and a pointer to the previous node.
- `head` and `tail` give direct access to both ends, so adding at either end takes constant time.
- `size` lets us validate indexes up front without walking the list.

## Code

Time complexity: `O(1)`-`O(n)`  
Space complexity: `O(n)`

```python
# Python 3
class ListNode:

    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or self.size == 0:
            return -1

        cur = self.head
        count = 0

        while cur and count <= index:
            if count == index:
                return cur.val

            cur = cur.next
            count += 1

        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val, self.head)

        self.head = new_node
        self.size += 1

        if self.head.next:
            self.head.next.prev = self.head
        else:
            self.tail = self.head

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
            return

        new_node = ListNode(val, None, self.tail)

        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        elif index == self.size:
            self.addAtTail(val)
            return
        elif index <= 0:
            self.addAtHead(val)
            return
        else:
            new_node = ListNode(val)

            cur = self.head
            for i in range(self.size):
                if i == index:
                    new_node.prev, new_node.next = cur.prev, cur
                    cur.prev.next = new_node
                    cur.prev = new_node
                    self.size += 1
                    return

                cur = cur.next

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size - 1:
            return
        elif index == 0:
            self.head = self.head.next
            self.size -= 1

            if self.head:
                self.head.prev = None
            else:
                self.tail = None

            return
        elif index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return
        else:
            cur = self.head
            for i in range(self.size):
                if i == index:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    self.size -= 1
                    return

                cur = cur.next
```
