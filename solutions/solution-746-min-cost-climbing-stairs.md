# 746. Min Cost Climbing Stairs

Let $f(i)$ be the cost you have to pay if you jump from step $i$. It is equal to the cost on $i$, plus the minimum of the cost for one step away and the cost for two steps away, i.e.

$f(i) = \texttt{cost[i]} + \min\{f(i-1), f(i-2)\}$.

For $i=0$, we have $f(i)=\texttt{cost[0]}$, i.e. if you jump from step $0$ you have to pay the cost assigned to step $0$, but you have nothing else to pay. For $i=1$, $f(i)=\texttt{cost[1]}$, i.e. if you jump from step $1$ then you just have to pay the cost assigned to $i=1$, but again you do not have any other obligations. But if you jump from $i=2$, then not only you have to pay the cost at step $2$, but you also should pay additional fees because you arrived at $i=2$ through either step $i=0$ or step $i=1$, and any of them has a cost. 

Remember the goal is to jump _out_ of the array. The final jump must be from the last step (element) or the second-to-last step (element). Once we calculated the value of $f$ for $i=0,1,\ldots,n-1$, we can then find which one has the minimal value, and this value is the output we are searching for. 

Simple Python code:

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            f.append(cost[i] + min(f[i-1], f[i-2]))
        return min(f[-1], f[-2])
```
