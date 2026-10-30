# 74. Search a 2D Matrix

**Difficulty:** `Medium`  
**Topics:** `Array` `Binary Search` `Matrix`

You are given an `m x n` integer matrix `matrix` with the following two properties:

- Each row is sorted in non-decreasing order
- The first integer of each row is greater than the last integer of the previous row

Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise.

You must write a solution in `O(log(m * n))` time complexity.

## Explanation

We can binary search the matrix as if it were a flat 1D array, without actually building that array, since reading it row by row,
left to right, gives one sorted sequence of `m * n` values.

We keep two pointers, `low` and `high`, as flat indices from `0` to `m * n - 1`. `mid` is the middle index between them, rounded down. To read its value, we convert `mid` back to a cell:

- `row = mid // n` (how many full rows come before it)
- `col = mid % n` (its position inside that row)

While `low <= high`:

- If `matrix[row][col] == target`, return `true`.
- If `target > matrix[row][col]`, the target can only be to the right, so move `low` to `mid + 1`.
- Otherwise, the target can only be to the left, so move `high` to `mid - 1`.

We skip `mid` itself (`+ 1` / `- 1`) because it has already been checked. If the loop ends with `low > high`, the search range is empty and `target` is not in the matrix, so return `false`.

## Code

Time complexity: `O(log(m*n))`  
Space complexity: `O(1)`

```python
# Python 3
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n = len(matrix[0])
        low, high = 0, (len(matrix) * n) - 1

        while low <= high:
            mid = (low + high) // 2
            row, col = mid // n, mid % n

            if target > matrix[row][col]:
                low = mid + 1
            elif target < matrix[row][col]:
                high = mid - 1
            else:
                return True

        return False
```
