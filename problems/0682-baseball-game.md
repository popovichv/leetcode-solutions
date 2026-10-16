# 682. Baseball Game

**Difficulty:** `Easy`  
**Topics:** `Array` `Stack`

You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start
with an empty record. You are given a list of strings `operations`, where `operations[i]` is the `i`th operation
you must apply to the record and is one of the following:

- An integer `x` - Record a new score of `x`.
- '+' - Record a new score that is the sum of the previous two scores.
- 'D' - Record a new score that is the double of the previous score.
- 'C' - Invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.

## Explanation

Create an array `scores` and use it as a stack.

For each operation:

- If "C": pop the last score
- If "D": push double of the last score
- If "+": push the sum of the last two scores
- Number: convert to an integer and push it

Return sum of `scores`.

## Code

Time complexity: `O(n)`  
Space complexity: `O(n)`

```python
# Python 3
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        scores = []

        for op in operations:
            if op == "C":
                scores.pop()
            elif op == "D":
                scores.append(scores[-1] * 2)
            elif op == "+":
                scores.append(scores[-1] + scores[-2])
            else:
                scores.append(int(op))

        return sum(scores)
```
