# Solution 1
import numpy as np

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        f = np.zeros(shape=(n,n), dtype=bool)
        for i in range(n-1, -1, -1):
            f[i, i] = True
            for j in range(i+1, n):
                if j == i+1 and s[i]==s[j]:
                    f[i, j] = True
                if j>i+1 and f[i+1, j-1] and s[i]==s[j]:
                    f[i, j] = True
        return np.sum(f)


# Solution 2
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        count = 0
        for i in range(len(s)-1, -1, -1):
            dp[i][i] = True
            count += 1
            for j in range(i+1, len(s)):
                if j == i+1 and s[i]==s[j]:
                    dp[i][j] = True
                    count += 1
                if j>i+1 and dp[i+1][j-1] and s[i]==s[j]:
                    dp[i][j] = True
                    count += 1
        return count