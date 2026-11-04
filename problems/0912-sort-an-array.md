# 912. Sort an Array

**Difficulty:** `Medium`  
**Topics:** `Array` `Sorting` `Merge Sort`

Given an array of integers `nums`, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in `O(nlog(n))` time complexity and with the smallest space complexity possible.

## Explanation

Merge sort recursively splits the array in half (by index ranges, not by creating new arrays) until each range has at most one element,
which is sorted by definition.

Then it merges neighboring ranges back together. Since both halves are already sorted, two pointers can compare their front elements
and always write the smaller one next. After one half runs out, the rest of the other half is copied over. Repeating this up the recursion produces a fully sorted array.

## Code

Time complexity: `O(n*logn)`  
Space complexity: `O(n)`

```python
# Python 3
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, arr: list[int], start: int, end: int) -> list[int]:
        if (end - start + 1) <= 1:
            return arr

        middle = (start + end) // 2
        self.mergeSort(arr, start, middle)
        self.mergeSort(arr, middle + 1, end)

        self.merge(arr, start, middle, end)

        return arr

    def merge(self, arr: list[int], start: int, middle: int, end: int) -> None:
        first = arr[start:middle+1]
        second = arr[middle+1:end+1]

        i, j = 0, 0
        w = start
        while i < len(first) and j < len(second):
            if first[i] <= second[j]:
                arr[w] = first[i]
                i += 1
            else:
                arr[w] = second[j]
                j += 1

            w += 1


        while j < len(second):
            arr[w] = second[j]
            j += 1
            w += 1

        while i < len(first):
            arr[w] = first[i]
            i += 1
            w += 1
```
