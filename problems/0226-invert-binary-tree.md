# 226. Invert Binary Tree

**Difficulty:** `Easy`  
**Topics:** `Tree` `Binary Tree` `DFS` `BFS`

Given the `root` of a binary tree, invert the tree, and return its root.

## Explanation

To invert a binary tree, we swap the left and right children of every node.

We do it recursively: swap the root's left and right children, then recursively invert each subtree. An empty node (`None`) is the base case and is returned as is.

## Code

Time complexity: `O(n)`  
Space complexity: `O(h)`

```python
# Python 3
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
```
