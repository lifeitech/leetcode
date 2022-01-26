class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        return sum([list(c) != sorted(c) for c in zip(*A)])