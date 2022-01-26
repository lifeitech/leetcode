# 746. Min Cost Climbing Stairs

Let <img src='https://latex.codecogs.com/svg.image?f(i)' title='f(i)' /> be the cost you have to pay if you jump from step <img src='https://latex.codecogs.com/svg.image?i' title='i' />. It is equal to the cost on <img src='https://latex.codecogs.com/svg.image?i' title='i' />, plus the minimum of the cost for one step away and the cost for two steps away, i.e.

<img src='https://latex.codecogs.com/svg.image?f(i)&space;=&space;\texttt{cost[i]}&space;&plus;&space;\min\{f(i-1),&space;f(i-2)\}' title='f(i)&space;=&space;\texttt{cost[i]}&space;&plus;&space;\min\{f(i-1),&space;f(i-2)\}' />.

For <img src='https://latex.codecogs.com/svg.image?i=0' title='i=0' />, we have <img src='https://latex.codecogs.com/svg.image?f(i)=\texttt{cost[0]}' title='f(i)=\texttt{cost[0]}' />, i.e. if you jump from step <img src='https://latex.codecogs.com/svg.image?0' title='0' /> you have to pay the cost assigned to step <img src='https://latex.codecogs.com/svg.image?0' title='0' />, but you have nothing else to pay. For <img src='https://latex.codecogs.com/svg.image?i=1' title='i=1' />, <img src='https://latex.codecogs.com/svg.image?f(i)=\texttt{cost[1]}' title='f(i)=\texttt{cost[1]}' />, i.e. if you jump from step <img src='https://latex.codecogs.com/svg.image?1' title='1' /> then you just have to pay the cost assigned to <img src='https://latex.codecogs.com/svg.image?i=1' title='i=1' />, but again you do not have any other obligations. But if you jump from <img src='https://latex.codecogs.com/svg.image?i=2' title='i=2' />, then not only you have to pay the cost at step <img src='https://latex.codecogs.com/svg.image?2' title='2' />, but you also should pay additional fees because you arrived at <img src='https://latex.codecogs.com/svg.image?i=2' title='i=2' /> through either step <img src='https://latex.codecogs.com/svg.image?i=0' title='i=0' /> or step <img src='https://latex.codecogs.com/svg.image?i=1' title='i=1' />, and any of them has a cost. 

Remember the goal is to jump _out_ of the array. The final jump must be from the last step (element) or the second-to-last step (element). Once we calculated the value of <img src='https://latex.codecogs.com/svg.image?f' title='f' /> for <img src='https://latex.codecogs.com/svg.image?i=0,1,\ldots,n-1' title='i=0,1,\ldots,n-1' />, we can then find which one has the minimal value, and this value is the output we are searching for. 

Simple Python code:

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            f.append(cost[i] + min(f[i-1], f[i-2]))
        return min(f[-1], f[-2])
```
