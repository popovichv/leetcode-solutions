# 110. Balanced Binary Tree

**Difficulty:** `Easy`  
**Topics:** `Tree` `Binary Tree` `DFS`

Given a binary tree, determine if it is height-balanced.

## Explanation

Use a bottom-up DFS that returns each subtree's height, or `-1` if it is unbalanced.

- Empty node: height `0`.
- If either child returns `-1`, or their heights differ by more than 1, return `-1`.
- Otherwise, return `1 + max(left, right)`.

The tree is balanced if the root's result is not `-1`. Each node is visited once.

## Code

Time complexity: `O(n)`  
Space complexity: `O(h)`

```python
# Python 3
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def getHeight(root):
            if not root:
                return 0

            hleft = getHeight(root.left)
            if hleft == -1:
                return -1

            hright = getHeight(root.right)
            if hright == -1:
                return -1

            if abs(hleft - hright) > 1:
                return -1

            return 1 + max(hleft, hright)

        return getHeight(root) != -1
```
