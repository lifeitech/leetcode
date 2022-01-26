import math

class Solution:
    def numSquares(self, n: int) -> int:
        f = [0, 1]
        for m in range(2, n+1):
            f.append(1 + min([f[m - i**2] for i in range(1, math.floor(math.sqrt(m))+1)]))
        return f[n]