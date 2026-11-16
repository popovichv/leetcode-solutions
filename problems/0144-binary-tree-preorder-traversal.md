# 144. Binary Tree Preorder Traversal

**Difficulty:** `Easy`  
**Topics:** `Tree` `Binary Tree` `DFS`

Given the `root` of a binary tree, return the preorder traversal of its nodes' values.

## Explanation

Preorder traversal visits nodes in the order **node, left, right**.

We use a recursive helper. For each node, we first add the node's value, then traverse its left subtree, then traverse its right subtree. An empty node (`None`) is the base case, so we just return.

## Code

Time complexity: `O(n)`  
Space complexity: `O(n)`

```python
# Python 3
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []

        def visit(root):
            if root:
                result.append(root.val)
                visit(root.left)
                visit(root.right)

        visit(root)
        return result
```
