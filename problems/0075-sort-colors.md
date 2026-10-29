# 75. Sort Colors

**Difficulty:** `Medium`  
**Topics:** `Array` `Counting Sort` `Dutch National Flag Algorithm`

You are given an array `nums` with `n` objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

## Explanation

### Counting Sort Method

Counting sort works well when values fall in a small known range. Here there are only three values (0, 1, 2),
so we count how many times each one occurs, then overwrite `nums` from left to right: `counts[0]` zeros, then
`counts[1]` ones, then `counts[2]` twos.

### Dutch National Flag Algorithm Method

This solves the problem in one pass using three pointers that split the array into four regions:

`mid` scans the unchecked region until it meets `high`. At each step we look at `nums[mid]`:

- `1`: already in the right place, so move `mid` forward.
- `0`: swap it with `nums[low]`, then move both `low` and `mid` forward. The value swapped
  into `mid` came from the `1`s region (or is the same element when `low == mid`), so it's safe to skip.
- `2`: swap it with `nums[high]`, then move `high` back. Don't move `mid`, because the value
  swapped in came from the unchecked region and still needs to be checked.

The loop ends when `mid > high`, meaning the unchecked region is empty.

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

### Dutch National Flag Algorithm Method

Time complexity: `O(n)`
Space complexity: `O(1)`

```python
# Python 3
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 1:
                mid += 1
            elif nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
```
