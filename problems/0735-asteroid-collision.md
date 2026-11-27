# 735. Asteroid Collision

**Difficulty:** `Medium`  
**Topics:** `Array` `Stack` `Simulation`

We are given an array `asteroids` of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

## Explanation

Use a stack to hold the asteroids that have survived so far. A collision only happens when the top of the stack moves right (`> 0`) and the current asteroid moves left (`< 0`).

While that is true, compare their sizes:

- If the top is smaller, it explodes. Pop it and keep checking against the new top.
- If they are equal, both explode. Pop the top and drop the current asteroid.
- If the top is bigger, the current asteroid explodes.

If the current asteroid survives, push it onto the stack. Whatever is left on the stack at the end is the answer.

## Code

Time complexity: `O(n)`  
Space complexity: `O(n)`

```python
# Python 3
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for ast in asteroids:
            alive = True

            while alive and stack and stack[-1] > 0 and ast < 0:
                if stack[-1] < -ast:
                    stack.pop()
                elif stack[-1] == -ast:
                    stack.pop()
                    alive = False
                else:
                    alive = False

            if alive:
                stack.append(ast)

        return stack
```
