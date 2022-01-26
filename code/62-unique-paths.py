from scipy.special import comb
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m+n-2, m-1, exact=True)