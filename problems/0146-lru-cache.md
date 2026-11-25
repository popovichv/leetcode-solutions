# 146. LRU Cache

**Difficulty:** `Medium`  
**Topics:** `Hash Table` `Doubly-Linked List` `Design`

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with **positive** size `capacity`.
- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.
- `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, **evict** the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.

## Explanation

We keep a hashmap that maps each key to a node in a doubly linked list. Two dummy nodes, `left` and `right`, mark the ends of
the list: `left.next` is the least recently used node, and `right.prev` is the most recently used one.

Whenever a key is used, we remove its node from the list and insert it right before `right`, making it the most recent. In `put`, after inserting, if the hashmap size exceeds the capacity, we evict `left.next` (the LRU node) from both the list and the hashmap.

## Code

Time complexity: `O(1)`
Space complexity: `O(n)`

```python
# Python 3
class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)
```
