class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[i ^ 1 for i in a[::-1]] for a in A]