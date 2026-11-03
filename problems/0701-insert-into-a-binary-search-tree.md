# 701. Insert Into a Binary Search Tree

**Difficulty:** `Medium`  
**Topics:** `Tree` `Binary Search Tree` `Binary Tree`

You are given the `root` node of a binary search tree (BST) and a `value` to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

## Explanation

We recursively walk down the tree, going left if `val` is smaller than the current node and right if it is greater.
When we reach an empty spot (`None`), we return a new node with `val`. The caller assigns that returned node to its `left` or `right` child, which links it into the tree. Every call returns its own `root`, so the existing structure is preserved on the way back up.

## Code

Time complexity: `O(h)`  
Space complexity: `O(h)`

```python
# Python 3
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)

        return root
```
