# 235. Lowest Common Ancestor of a Binary Search Tree

**Difficulty:** `Medium`  
**Topics:** `Tree` `Binary Tree` `DFS` `Lowest Common Ancestor`

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).”

## Explanation

### Path Comparison Method

1. Build the path to each node. Starting at the root, we use the BST property to walk toward the target: go left if the target is smaller than the current node, right if it is larger. Every node we pass is added to a list, and the target itself is added last. This gives the full path from the root down to the node.
2. Compare the two paths. Both paths start at the root and share the same nodes until they split. We walk through them side by side with `zip`, and the last node they have in common is the LCA.

If one node is an ancestor of the other, its path is shorter. `zip` stops at the end of the shorter path without finding a mismatch, so the LCA is that node itself, which matches the definition.

## Code

### Path Comparison Method

Time complexity: `O(h)`  
Space complexity: `O(h)`

```python
# Python 3
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findAncestors(root, val):
            ancestors = []
            while root.val != val:
                ancestors.append(root)
                if root.val > val:
                    root = root.left
                else:
                    root = root.right

            ancestors.append(root)
            return ancestors

        path_p = findAncestors(root, p.val)
        path_q = findAncestors(root, q.val)

        lca = root
        for a, b in zip(path_p, path_q):
            if a is b:
                lca = a
            else:
                break

        return lca
```
