# 706. Design HashMap

**Difficulty:** `Medium`  
**Topics:** `Array` `HashMap` `Linked List` `Design`

Design a HashMap without using any built-in hash table libraries.

Implement the `MyHashMap` class:

- `MyHashMap()` initializes the object with an empty map.
- `void put(int key, int value)` inserts a `(key, value)` pair into the HashMap. If the `key` already exists in the map, update the corresponding `value`.
- `int get(int key)` returns the `value` to which the specified `key` is mapped, or `-1` if this map contains no mapping for the `key`.
- `void remove(key)` removes the `key` and its corresponding `value` if the map contains the mapping for the `key`.

## Explanation

The map is an array of "buckets", where each bucket holds a linked list of elements with the same hash (chaining). A key goes to bucket `key % capacity`.

- `put`: walk the bucket's chain. If the key exists, update its value. Otherwise, append a new node at the tail and increase `size`.
- `get`: walk the bucket's chain and return the value on a match, or `-1` if the key isn't found.
- `remove`: if the head matches, point the bucket at `head.next`. Otherwise, walk the chain keeping a `prev` pointer and unlink the match with `prev.next = node.next`.

To keep chains short, the table resizes when `size` exceeds half the capacity (load factor 0.5). `rehash` doubles the capacity and reinserts every node. This step is required because each key's bucket index depends on `capacity`, so it changes after a resize.

## Code

Time complexity: `O(1)` - `O(n)`
Space complexity: `O(n)`

```python
# Python 3
class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 0
        self.capacity = 5000
        self.map = [None] * self.capacity

    def rehash(self):
        self.capacity *= 2
        self.size = 0
        old_map = self.map
        self.map = [None] * self.capacity

        for node in old_map:
            while node:
                self.put(node.key, node.val)
                node = node.next

    def put(self, key: int, value: int) -> None:
        idx = key % self.capacity

        if not self.map[idx]:
            self.map[idx] = Node(key, value)
        else:
            node = self.map[idx]
            while node:
                if node.key == key:
                    node.val = value
                    return
                prev = node
                node = node.next

            prev.next = Node(key, value)

        self.size += 1

        if self.size > self.capacity // 2:
            self.rehash()

    def get(self, key: int) -> int:
        idx = key % self.capacity

        node = self.map[idx]
        while node:
            if node.key == key:
                return node.val
            node = node.next

        return -1

    def remove(self, key: int) -> None:
        idx = key % self.capacity

        if not self.map[idx]:
            return

        node = self.map[idx]
        if node.key == key:
            self.map[idx] = node.next
            self.size -= 1
        else:
            while node:
                if node.key == key:
                    prev.next = node.next
                    self.size -= 1
                    return
                prev = node
                node = node.next
```
