class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return list([a[j] for a in A] for j in range(len(A[0])))