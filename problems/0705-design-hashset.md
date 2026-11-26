# 705. Design HashSet

**Difficulty:** `Easy`  
**Topics:** `Array` `HashSet` `Linked List` `Design`

Design a HashSet without using any built-in hash table libraries.

Implement the `MyHashSet` class:

- `void add(key)` inserts the value `key` into the HashSet.
- `bool contains(key)` returns whether the value `key` exists in the HashSet or not.
- `void remove(key)` removes the value `key` from the HashSet. If `key` does not exist in the HashSet, do nothing.

## Explanation

The set is an array of "buckets", where each bucket holds a linked list of keys with the same hash (chaining). A key goes to bucket `key % capacity`. It works like a HashMap, except each node stores only a key, with no value.

- `add`: walk the bucket's chain. If the key already exists, do nothing. Otherwise, append a new node at the tail and increase `size`.
- `contains`: walk the bucket's chain and return `True` on a match, or `False` if the key isn't found.
- `remove`: if the head matches, point the bucket at `head.next`. Otherwise, walk the chain keeping a `prev` pointer and unlink the match with `prev.next = node.next`.

To keep chains short, the table resizes when `size` exceeds half the capacity (load factor 0.5). `rehash` doubles the capacity and reinserts every node. This step is required because each key's bucket index depends on `capacity`, so it changes after a resize.

## Code

Time complexity: `O(1)` - `O(n)`  
Space complexity: `O(n)`

```python
# Python 3
class Node:

    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.size = 0
        self.capacity = 5000
        self.set = [None] * self.capacity

    def rehash(self):
        self.capacity *= 2
        self.size = 0
        old_set = self.set
        self.set = [None] * self.capacity

        for node in old_set:
            while node:
                self.add(node.key)
                node = node.next

    def add(self, key: int) -> None:
        idx = key % self.capacity

        if not self.set[idx]:
            self.set[idx] = Node(key)
        else:
            node = self.set[idx]
            while node:
                if node.key == key:
                    return
                prev = node
                node = node.next

            prev.next = Node(key)

        self.size += 1

        if self.size > self.capacity // 2:
            self.rehash()

    def remove(self, key: int) -> None:
        idx = key % self.capacity

        if not self.set[idx]:
            return

        node = self.set[idx]
        if node.key == key:
            self.set[idx] = node.next
            self.size -= 1
        else:
            while node:
                if node.key == key:
                    prev.next = node.next
                    self.size -= 1
                    return
                prev = node
                node = node.next

    def contains(self, key: int) -> bool:
        idx = key % self.capacity
        node = self.set[idx]

        while node:
            if node.key == key:
                return True
            node = node.next

        return False
```
