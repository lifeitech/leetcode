# 279. Perfect Squares

Let <img src='https://latex.codecogs.com/svg.image?f(n)' title='f(n)' /> be the function we are trying to compute. The dynamic programming relation is

<img src='https://latex.codecogs.com/svg.image?f(n)&space;=&space;1&space;&plus;&space;\min_{1\leq&space;i\leq\sqrt{n}}\left\{&space;f(n-i^2)&space;\right\}' title='f(n)&space;=&space;1&space;&plus;&space;\min_{1\leq&space;i\leq\sqrt{n}}\left\{&space;f(n-i^2)&space;\right\}' />.

Namely, we can decompose <img src='https://latex.codecogs.com/svg.image?n' title='n' /> as <img src='https://latex.codecogs.com/svg.image?n&space;=&space;i^2&space;&plus;&space;(n&space;-&space;i^2)' title='n&space;=&space;i^2&space;&plus;&space;(n&space;-&space;i^2)' /> for some <img src='https://latex.codecogs.com/svg.image?1\leq&space;i\leq\sqrt{n}' title='1\leq&space;i\leq\sqrt{n}' />. Any such <img src='https://latex.codecogs.com/svg.image?i' title='i' /> will increase the count by one, and we just need to select the <img src='https://latex.codecogs.com/svg.image?i' title='i' /> for which <img src='https://latex.codecogs.com/svg.image?f' title='f' /> has the smallest value on the remaining part <img src='https://latex.codecogs.com/svg.image?(n-i^2)' title='(n-i^2)' />.

The Python code is below.

```python
import math

class Solution:
    def numSquares(self, n: int) -> int:
        f = [0, 1]
        for m in range(2, n+1):
            f.append(1 + min([f[m - i**2] for i in range(1, math.floor(math.sqrt(m))+1)]))
        return f[n]
```
