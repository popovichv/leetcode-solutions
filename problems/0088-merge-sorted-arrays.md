# 88. Merge Sorted Arrays

**Difficulty:** `Easy`  
**Topics:** `Array` `Two Pointers` `Sorting`

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`,
representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this,
`nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements
are set to `0` and should be ignored. `nums2` has a length of `n`.

## Explanation

To avoid shifting elements to the right on every insertion, we merge from the end. The free space in `nums1` is at the back, so we can
write the largest elements there without overwriting anything we still need.

We use three pointers:

- `i`: the last real element of `nums1`
- `j`: the last element of `nums2`
- `w`: the position where we write

At each step we write the larger of `nums1[i]` and `nums2[j]` at position `w`, then move that pointer and `w` one step left.

We loop while `nums2` still has elements (`j >= 0`). Once `nums2` is iterated through, everything left in `nums1` is already sorted and
in its final place, so we can stop. The check `i >= 0` stops us from reading `nums1` after its real elements run out. In that case
the remaining elements of `nums2` are copied in.

## Code

Time complexity: `O(m + n)`  
Space complexity: `O(1)`

```python
# Python 3
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        w = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[w] = nums1[i]
                i -= 1
            else:
                nums1[w] = nums2[j]
                j -= 1

            w -= 1
```
