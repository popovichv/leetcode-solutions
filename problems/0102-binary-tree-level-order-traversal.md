# 102. Binary Tree Level Order Traversal

**Difficulty:** `Medium`  
**Topics:** `Tree` `Binary Tree` `BFS`

Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

## Explanation

Use BFS with a queue, starting from the root. At the start of each iteration, the queue holds exactly the nodes of the current level,
so `len(queue)` is that level's size. Pop that many nodes, add their values to a `level` list, and push their non-null children
onto the queue (left before right, which keeps the left-to-right order). After the level is processed, append `level` to the result.
Repeat until the queue is empty.

## Code

Time complexity: `O(n)`  
Space complexity: `O(n)`

```python
# Python 3
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        queue = deque([root])
        levels = []

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            levels.append(level)

        return levels
```
