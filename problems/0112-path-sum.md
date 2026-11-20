# 112. Path Sum

**Difficulty:** `Easy`  
**Topics:** `Tree` `Binary Tree` `DFS`

Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a root-to-leaf path such that adding up all the values along the path equals `targetSum`.

## Explanation

Use DFS and subtract each node's value from `targetSum` on the way down. That way, each recursive call only has to answer one question: is there a path from this node whose sum equals the remaining value?

- Empty node: return `false`, since there is no path.
- Leaf node: the path ends here, so check whether `root.val` equals the remaining sum.
- Otherwise: subtract `root.val` and check both subtrees. `or` short-circuits, so the search stops at the first valid path.

## Code

Time complexity: `O(n)`  
Space complexity: `O(h)`

```python
# Python 3
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        remains = targetSum - root.val
        return self.hasPathSum(root.left, remains) or self.hasPathSum(root.right, remains)
```
