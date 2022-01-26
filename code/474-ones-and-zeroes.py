class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)] 
        for s in strs:
            count_0 = s.count('0')
            count_1 = len(s)-count_0
            for i in range(m, count_0-1, -1):
                for j in range(n, count_1-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-count_0][j-count_1] + 1)
        return dp[m][n]