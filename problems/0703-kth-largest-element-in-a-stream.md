# 703. Kth Largest Element in a Stream

**Difficulty:** `Easy`
**Topics:** `Tree` `Heap` `Design`

You are part of a university admissions office and need to keep track of the `kth` highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer `k`, maintains a stream of test scores and continuously returns the `kth` highest test score after a new score has been submitted. More specifically, we are looking for the `kth` highest score in the sorted list of all scores.

Implement the `KthLargest` class:

`KthLargest(int k, int[] nums)` Initializes the object with the integer `k` and the stream of test scores `nums`.
`int add(int val)` Adds a new test score `val` to the stream and returns the element representing the `kth` largest element in the pool of test scores so far.

## Explanation

The k-th largest element is the smallest of the top k elements. So we keep a min-heap of exactly k elements, and its root (`heap[0]`) is always the answer.

1. Init: heapify `nums`, then pop the smallest elements until only `k` remain. Those removed values can never be the k-th largest again, since new values only push the cutoff up.
2. Add:
   - If the heap has fewer than `k` elements, push `val`.
   - If `val > heap[0]`, it belongs in the top k, so `heapreplace` swaps out the current smallest in one step.
   - Otherwise, `val` is too small to matter and we skip it.
3. Return `heap[0]`.

## Code

Time complexity: `O(logk - n*logn)`  
Space complexity: `O(k)`

```python
# Python 3
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.grades = nums
        heapify(self.grades)
        while len(self.grades) > self.k:
            heappop(self.grades)

    def add(self, val: int) -> int:
        if len(self.grades) < self.k:
            heappush(self.grades, val)
        elif val > self.grades[0]:
            heapreplace(self.grades, val)
        return self.grades[0]
```
