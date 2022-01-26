import numpy as np

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        if s == s[::-1]:
            return len(s)
        
        n = len(s)
        if  n == 0:
            return 0
        f = np.zeros(shape=(n,n), dtype=int)
        for i in range(n-1, -1, -1):
            f[i, i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    f[i, j] = 2 + f[i+1, j - 1]
                else:
                    f[i, j] = max(f[i+1, j], f[i, j - 1])
        return f[0, n-1]