# 983. Minimum Cost For Tickets

## Backward Solution

Let <img src='https://latex.codecogs.com/svg.image?f(i)' title='f(i)' /> be the minimal cost from day <img src='https://latex.codecogs.com/svg.image?i' title='i' /> to day <img src='https://latex.codecogs.com/svg.image?365' title='365' />, where <img src='https://latex.codecogs.com/svg.image?1\leq&space;i\leq&space;365' title='1\leq&space;i\leq&space;365' />. Standing on day <img src='https://latex.codecogs.com/svg.image?i' title='i' />, let's consider what we can do. If day <img src='https://latex.codecogs.com/svg.image?i' title='i' /> is not in our travel plan, then we have no reason to purchase ticket on this day. We can purchase tickets when we need them. Thus <img src='https://latex.codecogs.com/svg.image?f(i)&space;=&space;f(i&plus;1)' title='f(i)&space;=&space;f(i&plus;1)' />. If day <img src='https://latex.codecogs.com/svg.image?i' title='i' /> is in the travel plan, then we have three choices: 

1. We can spend `cost[0]` to satisfy the need on day <img src='https://latex.codecogs.com/svg.image?i' title='i' />. In this case <img src='https://latex.codecogs.com/svg.image?f(i)&space;=&space;\texttt{cost[0]}&space;&plus;&space;f(i&plus;1)' title='f(i)&space;=&space;\texttt{cost[0]}&space;&plus;&space;f(i&plus;1)' />.
2. We can spend `cost[1]` to get a 7-day pass. If we decide to do so, then for the consecutive 6 days we do not need to spend money again, so the total cost in the period <img src='https://latex.codecogs.com/svg.image?[i,&space;365]' title='[i,&space;365]' /> is equal to the cost of the 7-day pass plus the cost 7 days later. In this case <img src='https://latex.codecogs.com/svg.image?f(i)&space;=&space;\texttt{cost[1]}&space;&plus;&space;f(i&plus;7)' title='f(i)&space;=&space;\texttt{cost[1]}&space;&plus;&space;f(i&plus;7)' />.
3. We can spend `cost[2]` to get a 30-day pass. Then for 30 days we do not need to spend additional money, so the total cost in <img src='https://latex.codecogs.com/svg.image?[i,&space;365]' title='[i,&space;365]' /> is `cost[2]` plus <img src='https://latex.codecogs.com/svg.image?f(i&plus;30)' title='f(i&plus;30)' />.

Since <img src='https://latex.codecogs.com/svg.image?f(i)' title='f(i)' /> is optimal, we should select the one that has the least cost:

<img src='https://latex.codecogs.com/svg.image?f(i)&space;=&space;\min\left\{&space;\texttt{cost[0]}&plus;f(i&plus;1),~~\texttt{cost[1]}&plus;f(i&plus;7),~~\texttt{cost[2]}&plus;f(i&plus;30)\right\}' title='f(i)&space;=&space;\min\left\{&space;\texttt{cost[0]}&plus;f(i&plus;1),~~\texttt{cost[1]}&plus;f(i&plus;7),~~\texttt{cost[2]}&plus;f(i&plus;30)\right\}' />.

Of course, we cannot have days greater than <img src='https://latex.codecogs.com/svg.image?365' title='365' />, so in the code we should change 

* <img src='https://latex.codecogs.com/svg.image?i&plus;1' title='i&plus;1' /> to <img src='https://latex.codecogs.com/svg.image?\min(i&plus;1,&space;365)' title='\min(i&plus;1,&space;365)' />;
* <img src='https://latex.codecogs.com/svg.image?i&plus;7' title='i&plus;7' /> to <img src='https://latex.codecogs.com/svg.image?\min(i&plus;7,&space;365)' title='\min(i&plus;7,&space;365)' />;
* <img src='https://latex.codecogs.com/svg.image?i&plus;30' title='i&plus;30' /> to <img src='https://latex.codecogs.com/svg.image?\min(i&plus;30,&space;365)' title='\min(i&plus;30,&space;365)' />.

See code below.

```python
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
```

## Forward Solution

The foward solution is symmetric. Here we define <img src='https://latex.codecogs.com/svg.image?f(i)' title='f(i)' /> as the minimal cost from day <img src='https://latex.codecogs.com/svg.image?1' title='1' /> until <img src='https://latex.codecogs.com/svg.image?i' title='i' />. If day <img src='https://latex.codecogs.com/svg.image?i' title='i' /> is not in the travel plan, then again we have no reason to purchase ticket on this day. We may have purchased some tickets several days earlier, or we haven't purchased tickets for some days. In any case, <img src='https://latex.codecogs.com/svg.image?f(i)&space;=&space;f(i-1)' title='f(i)&space;=&space;f(i-1)' />, i.e. the two day should have the same cost. Remember here day <img src='https://latex.codecogs.com/svg.image?i' title='i' /> is the _last_ day we're considering. If day <img src='https://latex.codecogs.com/svg.image?i' title='i' /> is in the travel plan, then we should have purchased tickets earlier, otherwise we can purchase a 1-day pass to cover this last day. This corresponds to three costs <img src='https://latex.codecogs.com/svg.image?f(i-1)&space;&plus;&space;\texttt{cost[0]}' title='f(i-1)&space;&plus;&space;\texttt{cost[0]}' />, <img src='https://latex.codecogs.com/svg.image?f(i-7)&space;&plus;&space;\texttt{cost[1]}' title='f(i-7)&space;&plus;&space;\texttt{cost[1]}' />, and <img src='https://latex.codecogs.com/svg.image?f(i-30)&space;&plus;&space;\texttt{cost[2]}' title='f(i-30)&space;&plus;&space;\texttt{cost[2]}' /> respectively. By the optimality principle, the minimal one among the three should be <img src='https://latex.codecogs.com/svg.image?f(i)' title='f(i)' />:

<img src='https://latex.codecogs.com/svg.image?f(i)&space;=&space;\min\left\{f(i-1)&space;&plus;&space;\texttt{cost[0]},~~f(i-7)&space;&plus;&space;\texttt{cost[1]},~~f(i-30)&space;&plus;&space;\texttt{cost[2]}\right\}' title='f(i)&space;=&space;\min\left\{f(i-1)&space;&plus;&space;\texttt{cost[0]},~~f(i-7)&space;&plus;&space;\texttt{cost[1]},~~f(i-30)&space;&plus;&space;\texttt{cost[2]}\right\}' />.

This way we can calculate <img src='https://latex.codecogs.com/svg.image?f(i)' title='f(i)' /> in a forward fashion, from small <img src='https://latex.codecogs.com/svg.image?i' title='i' /> until the last day. Python code is below. Again, to prevent <img src='https://latex.codecogs.com/svg.image?i-1,&space;i-7' title='i-1,&space;i-7' /> and <img src='https://latex.codecogs.com/svg.image?i-30' title='i-30' /> from falling below <img src='https://latex.codecogs.com/svg.image?0' title='0' /> we change the dates to <img src='https://latex.codecogs.com/svg.image?\max(0,&space;i-1)' title='\max(0,&space;i-1)' />, <img src='https://latex.codecogs.com/svg.image?\max(0,&space;i-7)' title='\max(0,&space;i-7)' /> and <img src='https://latex.codecogs.com/svg.image?\max(0,&space;i-30)' title='\max(0,&space;i-30)' /> respectively.

```python
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        f= [0] * 366
        for i in range(366):
            if i not in days:
                f[i]=f[max(0, i-1)]
            else:
                f[i]=min(f[max(0, i-1)] + costs[0],
                         f[max(0, i-7)] + costs[1],
                         f[max(0, i-30)] + costs[2])
        return f[365]
```