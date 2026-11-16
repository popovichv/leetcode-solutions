# 590. N-ary Tree Postorder Traversal

**Difficulty:** `Easy`  
**Topics:** `Tree` `DFS`

Given the `root` of an n-ary tree, return the postorder traversal of its nodes' values.

## Explanation

Postorder traversal visits all of a node's **children first, then the node itself**. In an n-ary tree, a node can have any number of children, so instead of visiting `left` and `right`, we loop over the `children` list from left to right.

We use a recursive helper. For each node, we visit every child in order, and only after all of them are done we add the node's value. An empty node (`None`) is the base case, so we just return.

## Code

Time complexity: `O(n)`  
Space complexity: `O(n)`

```python
# Python 3
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []

        def visitChildren(root):
            if root:
                for child in root.children:
                    visitChildren(child)

                result.append(root.val)

        visitChildren(root)
        return result
```
