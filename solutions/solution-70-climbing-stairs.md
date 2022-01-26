# 70. Climbing Stairs

Suppose we are standing at stair $i$. For how we reached $i$, there are *two and only two* possibilities:

1. we were at stair $i-1$, and went up to stair $i$ by one step;

2. we were at stair $i-2$, and went up to stair $i$ by two steps.

Let $f(i)$ be the number of ways to get to stair $i$. Then we have

$f(i) = f(i-1) + f(i-2)$.

Namely, the number of ways to get to $i$ equals the number of ways to get to $i-1$ plus the number of ways to get to $i-2$.

Simple Python code:

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        f = [1, 2]
        for i in range(2, n):
            f.append(f[i-1] + f[i-2])
        return f[n-1]
```
