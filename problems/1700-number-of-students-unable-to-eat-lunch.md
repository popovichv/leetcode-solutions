# 1700. Number of Students Unable to Eat Lunch

**Difficulty:** `Easy`  
**Topics:** `Array` `Stack` `Queue`

The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers `0` and `1` respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

- If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
- Otherwise, they will leave it and go to the queue's end.

This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays `students` and `sandwiches` where `sandwiches[i]` is the type of the `i`​​​​​​th sandwich in the stack (`i = 0` is the top of the stack) and `students[j]` is the preference of the `j`​​​​​​th student in the initial queue (`j = 0` is the front of the queue). Return the number of students that are unable to eat.

## Explanation

BThe order of students doesn't matter. Only two things matter:

- How many students want 0 and how many want 1.
- The order of the sandwiches.

The first sandwich whose type has no students left wanting it blocks the stack, and everyone remaining can’t eat.

## Code

Time complexity: `O(n)`  
Space complexity: `O(1)`

```python
# Python 3
class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        count = [students.count(0), students.count(1)]

        for i, s in enumerate(sandwiches):
            if count[s] == 0:
                return len(sandwiches) - i
            count[s] -= 1

        return 0
```
