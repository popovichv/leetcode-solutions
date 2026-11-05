# 230. Kth Smallest Element in a BST

**Difficulty:** `Medium`  
**Topics:** `Tree` `Binary Tree` `DFS`

Given the `root` of a binary search tree, and an integer `k`, return the `k`th smallest value (1-indexed) of all the values of the nodes in the tree.

## Explanation

Inorder traversal of a BST visits values in sorted order, so the `k`th node visited is the answer.

Use an explicit stack to do inorder iteratively:

1. Go left as far as possible, pushing each node.
2. Pop a node and decrement `k`. If `k == 0`, return its value.
3. Move to its right subtree and repeat.

This stops as soon as the answer is found, and the stack only holds one root-to-node path.

## Code

Time complexity: `O(h + k)`  
Space complexity: `O(h)`

```python
# Python 3
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val

            root = root.right
```
