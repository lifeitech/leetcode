class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        f = [0] * len(A)
        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                f[i] = 1 + f[i-1]
        return sum(f)