# 169. Majority Element

**Difficulty:** `Easy`  
**Topics:** `Array` `Hash Table`

Given an array `nums` of size `n`, return the majority element. The majority element is the element that
appears more than `n / 2` times. You may assume that the majority element always exists in the array.

## Explanation

Use a hash map to count how many times each number appears, initialized with `defaultdict(int)` which treats any missing key
as having a count of `0`.

For every number in `nums`, increase its count by `1`. As soon as a count becomes greater than
`len(nums) // 2`, that number is the majority element, so return it right away.

## Code

Time complexity: `O(n)`  
Space complexity: `O(n)`

```python
# Python 3
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        element_count = defaultdict(int)

        for n in nums:
            element_count[n] += 1

            if element_count[n] > len(nums) // 2:
                return n
```
