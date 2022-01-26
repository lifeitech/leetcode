import numpy as np

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A); A = np.array(A)
        f = np.zeros(shape=(n, n), dtype=int)
        
        for j in range(n):
            f[n-1, j] = A[n-1, j]
        
        for i in range(n-2, -1, -1):
            for j in range(n):
                if  j == 0:
                    f[i, j] = A[i, j] + min(f[i+1, j], f[i+1, j+1])
                elif j == n-1:
                    f[i, j] = A[i, j] + min(f[i+1, j-1], f[i+1, j])
                else:
                    f[i, j] = A[i, j] + min(f[i+1, j-1], f[i+1, j], f[i+1, j+1])
        return min(f[0, :])