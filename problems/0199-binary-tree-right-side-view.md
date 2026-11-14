# 199. Binary Tree Right Side View

**Difficulty:** `Medium`  
**Topics:** `Tree` `Binary Tree` `BFS` `DFS`

Given the `root` of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

## Explanation

Use BFS with a queue, starting from the root. At the start of each iteration, the queue holds exactly the nodes of the current level,
so `len(queue)` is that level's size. Because children are pushed left before right, the last node in the queue (`queue[-1]`) is the
rightmost node of the level, so we append its value to the result. Then we pop all nodes of the level and push their non-null children
onto the queue. Repeat until the queue is empty.

## Code

Time complexity: `O(n)`  
Space complexity: `O(n)`

```python
# Python 3
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        rightest = []
        queue = deque([root])

        while queue:
            rightest.append(queue[-1].val)

            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return rightest
```
