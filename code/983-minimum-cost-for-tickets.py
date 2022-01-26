# Backward solution
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        f=[0] * 366
        for i in range(365, 0, -1):
            if i not in days:
                f[i]=f[min(i+1, 365)]
            else:
                f[i]=min(cost[0] + f[min(i+1, 365)], 
                         cost[1] + f[min(i+7, 365)], 
                         cost[2] + f[min(i+30, 365)])
        return f[1]


# Forward solution     
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        f= [0] * 366
        for i in range(366):
            if i not in days:
                f[i]=f[max(0,i-1)]
            else:
                f[i]=min(f[max(0,i-1)] + costs[0],
                         f[max(0,i-7)] + costs[1],
                         f[max(0,i-30)] + costs[2])
        return f[365]