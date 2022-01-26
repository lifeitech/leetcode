class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            f.append(cost[i] + min(f[i-1], f[i-2]))
        return min(f[-1], f[-2])