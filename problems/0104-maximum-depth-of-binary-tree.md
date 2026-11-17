# 104. Maximum Depth of Binary Tree

**Difficulty:** `Easy`  
**Topics:** `Tree` `Binary Tree` `DFS` `BFS`

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Explanation

The depth of a tree is 1 (for the root) plus the depth of its deeper subtree.

We use this recursively: an empty node (`None`) has depth 0, which is the base case. For any other node, we compute the depth of the left and right subtrees, take the larger one, and add 1 for the current node.

## Code

Time complexity: `O(n)`  
Space complexity: `O(h)`

```python
# Python 3
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```
