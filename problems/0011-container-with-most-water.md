# 11. Container With Most Water

**Difficulty:** `Medium`  
**Topics:** `Array` `Two Pointers`

You are given an integer array height of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

## Explanation

We place two pointers at the ends of the array, which gives the widest possible container. At each step we calculate the area as `min(height[left], height[right]) * (right - left)` and keep the maximum.

Then we move the pointer at the shorter line inward. The shorter line limits the water level, and moving inward always makes the width smaller. So keeping the shorter line can never give a bigger area. Moving it is the only way to find a taller line that might make up for the lost width.

## Code

Time complexity: `O(n)`  
Space complexity: `O(1)`

```python
class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_level = 0
        left, right = 0, len(height) - 1

        while left < right:
            current = min(height[left], height[right]) * (right - left)
            max_level = max(max_level, current)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_level
```
