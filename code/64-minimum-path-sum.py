
# Solution 1: from top to bottom
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

    
# Solution 2: from bottom to top
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