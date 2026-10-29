# 75. Sort Colors

**Difficulty:** `Medium`  
**Topics:** `Array` `Counting Sort`

You are given an array `nums` with `n` objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

## Explanation

### Counting Sort Method

Counting sort works well when values fall in a small known range. Here there are only three values (0, 1, 2),
so we count how many times each one occurs, then overwrite `nums` from left to right: `counts[0]` zeros, then
`counts[1]` ones, then `counts[2]` twos.

## Code

### Counting Sort Method

Time complexity: `O(n)`
Space complexity: `O(1)`

```python
# Python 3
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for n in nums:
            counts[n] += 1

        i = 0
        for x in range(len(counts)):
            for _ in range(counts[x]):
                nums[i] = x
                i += 1
```
