import numpy as np
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return np.argmax(A)