# 343. Integer Break

Let <img src='https://latex.codecogs.com/svg.image?f(n)' title='f(n)' /> be the maximal product of decompositions of <img src='https://latex.codecogs.com/svg.image?n' title='n' />. The Bellman equation is a little bit tricky:

<img src='https://latex.codecogs.com/svg.image?f(n)&space;=&space;\max\left\{&space;\max_{1\leq&space;j<n}\left\{j\cdot&space;f(n-j)\right\},\quad&space;j\cdot(n&space;-&space;j)\right\}' title='f(n)&space;=&space;\max\left\{&space;\max_{1\leq&space;j<n}\left\{j\cdot&space;f(n-j)\right\},\quad&space;j\cdot(n&space;-&space;j)\right\}' />.

Python code

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        f = [1 for _ in range(n + 1)]
        for m in range(2, n + 1):
            for j in range(1, m):
                f[m] = max(f[m], j * f[m - j], j * (m - j))
        return f[n]
```
