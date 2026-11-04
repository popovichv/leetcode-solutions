# 94. Binary Tree Inorder Traversal

**Difficulty:** `Easy`  
**Topics:** `Tree` `Binary Tree` `DFS`

Given the `root` of a binary tree, return the inorder traversal of its nodes' values.

## Explanation

Inorder traversal visits nodes in the order **left, node, right**.

We use a recursive helper. For each node, we first traverse its left subtree, then add the node's value to the result, then traverse its right subtree. An empty node (`None`) is the base case, so we just return.

## Code

Time complexity: `O(n)`  
Space complexity: `O(n)`

```python
# Python 3
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            result.append(root.val)
            inorder(root.right)

        inorder(root)
        return result
```
