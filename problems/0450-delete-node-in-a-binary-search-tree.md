# 450. Delete Node in a Binary Search Tree

**Difficulty:** `Medium`  
**Topics:** `Tree` `Binary Search Tree` `Binary Tree`

Given a `root` node reference of a BST and a `key`, delete the node with the given `key` in the BST. Return the `root` node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

- Search for a `node` to remove.
- If the `node` is found, delete the `node`.

## Explanation

We recursively search for the node, going left if `key` is smaller than the current node and right if it is greater. Like in insertion, each call returns its subtree's root, and the caller assigns it back to `left` or `right`, so the tree stays linked.

When we find the node, there are three cases:

- **No left child:** return the right child. It takes the deleted node's place (this also covers leaves, since the right child is then `None`).
- **No right child:** return the left child.
- **Two children:** find the in-order successor, the smallest node in the right subtree (go right once, then left as far as possible). Copy its value into the current node, then recursively delete the successor from the right subtree. The successor has no left child, so that deletion always falls into one of the simple cases above.

Using the successor keeps the BST property: its value is greater than everything in the left subtree and smaller than everything else in the right subtree.

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
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_node = root.right
                while min_node and min_node.left:
                    min_node = min_node.left

                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)

        return root
```
