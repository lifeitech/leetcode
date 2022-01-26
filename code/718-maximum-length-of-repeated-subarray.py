import numpy as np

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        f = np.zeros(shape=(m+1, n+1), dtype=int)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if A[i] == B[j]:
                    f[i, j] = f[i+1, j+1] + 1
        return f.max()