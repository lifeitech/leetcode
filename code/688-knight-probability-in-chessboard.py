class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        p = {(r, c): 1}
        for _ in range(K):
            p = {(r, c): sum(p.get((r+i, c+j), 0) + p.get((r+j, c+i), 0) for i in (1, -1) for j in (2, -2)) / 8 
                 for r in range(N) for c in range(N)}
        
        return sum(p.values())