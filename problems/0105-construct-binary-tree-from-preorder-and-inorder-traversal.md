# 105. Construct Binary Tree from Preorder and Inorder Traversal

**Difficulty:** `Medium`
**Topics:** `Array` `Tree` `Binary Tree`

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

## Explanation

### Recursive Method

1. Build a hashmap `index_inorder` that maps each value to its index in `inorder`.
2. Keep a pointer `pre` into `preorder`. The recursion creates nodes in the same order as preorder (root first, then the whole left subtree, then the right subtree), so each call just takes the next value and advances the pointer.
3. `build(left, right)` constructs the subtree covering `inorder[left..right]`:
   - If `left > right`, the range is empty, so return `None`.
   - Create the root from `preorder[pre]` and find its position `mid` in `inorder`.
   - Everything in `inorder[left..mid - 1]` belongs to the left subtree, and everything in `inorder[mid + 1..right]` belongs to the right subtree.
   - Build the left subtree **before** the right one. Otherwise the `pre` pointer would hand out left-subtree values to the right side.

Inorder decides the **shape** (subtree sizes, when a subtree is empty), and preorder decides the **values**.

### Iterative Method

The stack holds the nodes on the current path that do not have a right child yet. `inorder[ino]` is the next node that inorder would visit, which happens only after that node's left subtree is complete.

For each next value in `preorder`:

1. **Top of stack ≠ `inorder[ino]`:** the top still has a left subtree to build. Preorder goes left first, so the new node is the top's **left child**.
2. **Top of stack == `inorder[ino]`:** the top's left side is finished, so inorder visits it. Pop it and advance `ino`. Keep popping while the top matches, because several ancestors can finish at the same time. The new node is the **right child of the last popped node**: after visiting a node, inorder moves into its right subtree, and preorder supplies that subtree's root next.
3. Push the new node onto the stack.

In short: go left until inorder says stop, back up while inorder confirms nodes are finished, then turn right once.

## Code

### Recursive Method

Time complexity: `O(n)`  
Space complexity: `O(1)`

```python
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        index_inorder = {val: i for i, val in enumerate(inorder)}
        pre = 0

        def build(left, right):
            nonlocal pre

            if left > right:
                return None

            root = TreeNode(preorder[pre])
            pre += 1
            mid = index_inorder[root.val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)

```

### Iterative Method

Time complexity: `O(n)`  
Space complexity: `O(1)`

```python
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        root = TreeNode(preorder[0])
        stack = [root]

        ino = 0
        for i in range(1, len(preorder)):
            new_node = TreeNode(preorder[i])

            if stack[-1].val != inorder[ino]:
                stack[-1].left = new_node
            else:
                while stack and stack[-1].val == inorder[ino]:
                    parent = stack.pop()
                    ino += 1
                parent.right = new_node

            stack.append(new_node)

        return root
```
