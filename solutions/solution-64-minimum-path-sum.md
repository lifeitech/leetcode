# 64. Minimum Path Sum

This problem is a classic dynamic programming problem. We can solve this problem either from top to bottom or from bottom to top. Let's have a look at the two ways.

#### From top to bottom

Let <img src='https://latex.codecogs.com/svg.image?g' title='g' /> denote the grid and let <img src='https://latex.codecogs.com/svg.image?g(i,j)' title='g(i,j)' /> denote the grid value at index <img src='https://latex.codecogs.com/svg.image?(i,&space;j)' title='(i,&space;j)' />. For top to bottom, the value function <img src='https://latex.codecogs.com/svg.image?f(i,&space;j)' title='f(i,&space;j)' /> is defined as the optimal sum from <img src='https://latex.codecogs.com/svg.image?(0,&space;0)' title='(0,&space;0)' /> to <img src='https://latex.codecogs.com/svg.image?(i,&space;j)' title='(i,&space;j)' />. From the constraints given in the problem, we can come to <img src='https://latex.codecogs.com/svg.image?(i,&space;j)' title='(i,&space;j)' /> only through one of two cells: its top cell <img src='https://latex.codecogs.com/svg.image?(i-1,&space;j)' title='(i-1,&space;j)' /> or its left cell <img src='https://latex.codecogs.com/svg.image?(i,&space;j-1)' title='(i,&space;j-1)' />. The value <img src='https://latex.codecogs.com/svg.image?f(i,&space;j)' title='f(i,&space;j)' /> should be <img src='https://latex.codecogs.com/svg.image?g(i,&space;j)' title='g(i,&space;j)' /> plus the minimum of the two values at those two cells:

<img src='https://latex.codecogs.com/svg.image?f(i,&space;j)&space;=&space;g(i,&space;j)&space;&plus;&space;\min\{f(i-1,&space;j),&space;f(i,&space;j-1)\}' title='f(i,&space;j)&space;=&space;g(i,&space;j)&space;&plus;&space;\min\{f(i-1,&space;j),&space;f(i,&space;j-1)\}' />.

This way we fill the value table <img src='https://latex.codecogs.com/svg.image?f' title='f' /> from top left to bottom right, until we get the value <img src='https://latex.codecogs.com/svg.image?f(m-1,&space;n-1)' title='f(m-1,&space;n-1)' />. Since we are only allowed to move right and down, the values at the left and top boundaries can first be filled.

Below is the Python code. It is enough to modify the input so as to store the values, so we do not need to create a new table for <img src='https://latex.codecogs.com/svg.image?f' title='f' />.

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

We can also work out the problem from bottom to top. Here the definition of the value function <img src='https://latex.codecogs.com/svg.image?f' title='f' /> is different. <img src='https://latex.codecogs.com/svg.image?f(i,&space;j)' title='f(i,&space;j)' /> is the optimal value at <img src='https://latex.codecogs.com/svg.image?(i,&space;j)' title='(i,&space;j)' /> if we _start_  from <img src='https://latex.codecogs.com/svg.image?(i,&space;j)' title='(i,&space;j)' /> and go to the endpoint <img src='https://latex.codecogs.com/svg.image?(m-1,&space;n-1)' title='(m-1,&space;n-1)' />. At the position <img src='https://latex.codecogs.com/svg.image?(i,&space;j)' title='(i,&space;j)' />, we can only go to one of two cells: either its right <img src='https://latex.codecogs.com/svg.image?(i,&space;j&plus;1)' title='(i,&space;j&plus;1)' />, or its bottom <img src='https://latex.codecogs.com/svg.image?(i&plus;1,&space;j)' title='(i&plus;1,&space;j)' />. For the first choice, the value is <img src='https://latex.codecogs.com/svg.image?g(i,&space;j)&space;&plus;&space;f(i,&space;j&plus;1)' title='g(i,&space;j)&space;&plus;&space;f(i,&space;j&plus;1)' />, and for the second choice the value is <img src='https://latex.codecogs.com/svg.image?g(i,&space;j)&space;&plus;&space;f(i&plus;1,&space;j)' title='g(i,&space;j)&space;&plus;&space;f(i&plus;1,&space;j)' />. The minimum of the two values should be the value at the cell <img src='https://latex.codecogs.com/svg.image?(i,&space;j)' title='(i,&space;j)' />. So

<img src='https://latex.codecogs.com/svg.image?f(i,&space;j)&space;=&space;g(i,&space;j)&space;&plus;&space;\min\{f(i,&space;j&plus;1),&space;f(i&plus;1,&space;j)\}' title='f(i,&space;j)&space;=&space;g(i,&space;j)&space;&plus;&space;\min\{f(i,&space;j&plus;1),&space;f(i&plus;1,&space;j)\}' />.

The Python code is pasted below. Note its symmetry with the first one: in the above program <img src='https://latex.codecogs.com/svg.image?i' title='i' /> goes from <img src='https://latex.codecogs.com/svg.image?0' title='0' /> to <img src='https://latex.codecogs.com/svg.image?m-1' title='m-1' />, <img src='https://latex.codecogs.com/svg.image?j' title='j' /> goes from <img src='https://latex.codecogs.com/svg.image?0' title='0' /> to <img src='https://latex.codecogs.com/svg.image?n-1' title='n-1' />, while here <img src='https://latex.codecogs.com/svg.image?i' title='i' /> goes from <img src='https://latex.codecogs.com/svg.image?m-1' title='m-1' /> to <img src='https://latex.codecogs.com/svg.image?0' title='0' /> in reverse direction, and <img src='https://latex.codecogs.com/svg.image?j' title='j' /> goes from <img src='https://latex.codecogs.com/svg.image?n-1' title='n-1' /> to <img src='https://latex.codecogs.com/svg.image?0' title='0' /> in reverse direction.

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
