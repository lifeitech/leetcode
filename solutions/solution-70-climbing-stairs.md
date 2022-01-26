# 70. Climbing Stairs

Suppose we are standing at stair <img src='https://latex.codecogs.com/svg.image?i' title='i' />. For how we reached <img src='https://latex.codecogs.com/svg.image?i' title='i' />, there are *two and only two* possibilities:

1. we were at stair <img src='https://latex.codecogs.com/svg.image?i-1' title='i-1' />, and went up to stair <img src='https://latex.codecogs.com/svg.image?i' title='i' /> by one step;

2. we were at stair <img src='https://latex.codecogs.com/svg.image?i-2' title='i-2' />, and went up to stair <img src='https://latex.codecogs.com/svg.image?i' title='i' /> by two steps.

Let <img src='https://latex.codecogs.com/svg.image?f(i)' title='f(i)' /> be the number of ways to get to stair <img src='https://latex.codecogs.com/svg.image?i' title='i' />. Then we have

<img src='https://latex.codecogs.com/svg.image?f(i)&space;=&space;f(i-1)&space;&plus;&space;f(i-2)' title='f(i)&space;=&space;f(i-1)&space;&plus;&space;f(i-2)' />.

Namely, the number of ways to get to <img src='https://latex.codecogs.com/svg.image?i' title='i' /> equals the number of ways to get to <img src='https://latex.codecogs.com/svg.image?i-1' title='i-1' /> plus the number of ways to get to <img src='https://latex.codecogs.com/svg.image?i-2' title='i-2' />.

Simple Python code:

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        f = [1, 2]
        for i in range(2, n):
            f.append(f[i-1] + f[i-2])
        return f[n-1]
```
