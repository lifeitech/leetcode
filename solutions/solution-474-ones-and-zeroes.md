# 474. Ones and Zeroes

This is a knapsack problem. We have constrained capacity (<img src='https://latex.codecogs.com/svg.image?m' title='m' /> zeros and <img src='https://latex.codecogs.com/svg.image?n' title='n' /> ones) but we want to take as much items as possible. The problem can be solved using dynamic programming: suppose we have an optimal bag of items. If we remove any item from the bag, the remaining items must be optimal under the reduced capacity. 

Let <img src='https://latex.codecogs.com/svg.image?f(i,&space;j,&space;k)' title='f(i,&space;j,&space;k)' /> be the value function (the maximal number of items we can get) when we restrict to previous <img src='https://latex.codecogs.com/svg.image?k' title='k' /> items `strs[:k+1]` with capacity <img src='https://latex.codecogs.com/svg.image?i' title='i' /> zeros and <img src='https://latex.codecogs.com/svg.image?j' title='j' /> ones. For item <img src='https://latex.codecogs.com/svg.image?k' title='k' />, we have two choices: either take it or not take it. We should choose the option that yields highest value:

<img src='https://latex.codecogs.com/svg.image?f(i,&space;j,&space;k)&space;=&space;\max\left\{&space;f(i,&space;j,&space;k-1),\,\,&space;1&space;&plus;&space;f(i-k_0,&space;j-k_1,&space;k-1)\right\}' title='f(i,&space;j,&space;k)&space;=&space;\max\left\{&space;f(i,&space;j,&space;k-1),\,\,&space;1&space;&plus;&space;f(i-k_0,&space;j-k_1,&space;k-1)\right\}' />,

where <img src='https://latex.codecogs.com/svg.image?k_0' title='k_0' /> is the number of zeros in `strs[k]`, and <img src='https://latex.codecogs.com/svg.image?k_1' title='k_1' /> is the number of ones in `strs[k]`.

Python code below. The program has TLE.

```python
import numpy as np

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        f = np.zeros(shape=(m+1, n+1), dtype=int)

        for k in range(len(strs)):
            k0 = strs[k].count('0')
            k1 = strs[k].count('1')
            for i in range(m, k0 - 1, -1):
                for j in range(n, k1 - 1, -1):
                    f[i, j] = max(f[i, j], f[i - k0, j - k1] + 1)
        return f[m, n]
```

Note from the equation above that in implementation we don't have to maintain the third variable <img src='https://latex.codecogs.com/svg.image?k' title='k' />. We can optimize <img src='https://latex.codecogs.com/svg.image?f(i,&space;j)' title='f(i,&space;j)' /> over and over. In fact the specific order of the elements in `strs` does not matter. 