# 543. Diamiter of a Binary Tree

**Difficulty:** `Easy`  
**Topics:** `Tree` `Binary Tree` `DFS`

Given the `root` of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The length of a path between two nodes is represented by the number of edges between them.

## Explanation

Every path in a tree has one highest node where it "bends": it comes up from one subtree and goes down into the other. So we can find the longest path by checking every node as a possible bend point.

- Run a DFS where `getHeight(node)` returns the height of the subtree (the number of nodes on its longest downward path, `0` for an empty node).
- At each node, `left + right` is the number of edges in the longest path that bends at that node. Update `best` with it.
- Return `1 + max(left, right)` so the parent can use this node's height.

`best` ends up as the maximum over all nodes. Checking every node, not only the root, matters because the longest path may not pass through the root.

## Code

Time complexity: `O(n)`  
Space complexity: `O(h)`

```python
# Python 3
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def getHeight(root):
            nonlocal best

            if not root:
                return 0

            left = getHeight(root.left)
            right = getHeight(root.right)

            best = max(best, left + right)

            return 1 + max(left, right)

        getHeight(root)
        return best
```
