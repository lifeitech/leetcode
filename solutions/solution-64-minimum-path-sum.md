# 64. Minimum Path Sum

This problem is a classic dynamic programming problem. We can solve this problem either from top to bottom or from bottom to top. Let's have a look at the two ways.

#### From top to bottom

Let $g$ denote the grid and let $g(i,j)$ denote the grid value at index $(i, j)$. For top to bottom, the value function $f(i, j)$ is defined as the optimal sum from $(0, 0)$ to $(i, j)$. From the constraints given in the problem, we can come to $(i, j)$ only through one of two cells: its top cell $(i-1, j)$ or its left cell $(i, j-1)$. The value $f(i, j)$ should be $g(i, j)$ plus the minimum of the two values at those two cells:

$f(i, j) = g(i, j) + \min\{f(i-1, j), f(i, j-1)\}$.

This way we fill the value table $f$ from top left to bottom right, until we get the value $f(m-1, n-1)$. Since we are only allowed to move right and down, the values at the left and top boundaries can first be filled.

Below is the Python code. It is enough to modify the input so as to store the values, so we do not need to create a new table for $f$.

```python
# from top to bottom
import numpy as np

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        g = np.array(grid)
        m, n = g.shape
        if m == 0 or n == 0:
            return 0
        for i in range(m):
            for j in range(n):
                if i == 0 and j != 0:
                    g[i, j] = g[i, j] + g[i, j-1]
                if i != 0 and j == 0:
                    g[i, j] = g[i, j] + g[i-1, j]
                if i != 0 and j != 0:
                    g[i, j] = g[i, j] + min(g[i, j-1], g[i-1, j])
        return g[m-1, n-1]
```

#### From bottom to top

We can also work out the problem from bottom to top. Here the definition of the value function $f$ is different. $f(i, j)$ is the optimal value at $(i, j)$ if we _start_  from $(i, j)$ and go to the endpoint $(m-1, n-1)$. At the position $(i, j)$, we can only go to one of two cells: either its right $(i, j+1)$, or its bottom $(i+1, j)$. For the first choice, the value is $g(i, j) + f(i, j+1)$, and for the second choice the value is $g(i, j) + f(i+1, j)$. The minimum of the two values should be the value at the cell $(i, j)$. So

$f(i, j) = g(i, j) + \min\{f(i, j+1), f(i+1, j)\}$.

The Python code is pasted below. Note its symmetry with the first one: in the above program $i$ goes from $0$ to $m-1$, $j$ goes from $0$ to $n-1$, while here $i$ goes from $m-1$ to $0$ in reverse direction, and $j$ goes from $n-1$ to $0$ in reverse direction.

```python
# from bottom to top
import numpy as np

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        g = np.array(grid)
        m, n = g.shape
        if m == 0 or n == 0:
            return 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j != n-1:
                    g[i, j] = g[i, j] + g[i, j+1]
                if i != m-1 and j == n-1:
                    g[i, j] = g[i, j] + g[i+1, j]
                if i != m-1 and j != n-1:
                    g[i, j] = g[i, j] + min(g[i, j+1], g[i+1, j])
        return g[0, 0]
```
