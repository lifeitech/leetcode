import numpy as np

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n % 2 == 0 or n == 1:
            return True
        f = np.zeros(shape=(n, n))
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                f[i, j] = max(nums[i] - f[i+1, j], nums[j] - f[i, j - 1])
        return f[0, -1] >= 0