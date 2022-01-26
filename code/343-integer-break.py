class Solution:
    def integerBreak(self, n: int) -> int:
        f = [1 for _ in range(n + 1)]
        for m in range(2, n + 1):
            for j in range(1, m):
                f[m] = max(f[m], j * f[m - j], j * (m - j))
        return f[n]