# 145. Binary Tree Postorder Traversal

**Difficulty:** `Easy`  
**Topics:** `Tree` `Binary Tree` `DFS`

Given the `root` of a binary tree, return the postorder traversal of its nodes' values.

## Explanation

Postorder traversal visits nodes in the order **left, right, node**.

We solve it recursively. An empty node (`None`) is the base case, so we return an empty list. Otherwise, we get the postorder list of the left subtree, then the list of the right subtree, and append the node's value at the end by concatenating the three lists.

## Code

Time complexity: `O(n)`
Space complexity: `O(n)`

```python
# Python 3
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
```
