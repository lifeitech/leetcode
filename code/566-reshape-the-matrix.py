import numpy as np
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        try:
            return np.reshape(nums, (r,c)).tolist()
        except ValueError:
            return nums