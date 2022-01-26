# 198. House Robber

Let <img src='https://latex.codecogs.com/svg.image?f(k)' title='f(k)' /> be the maximal amount of money you can get from the first <img src='https://latex.codecogs.com/svg.image?k' title='k' /> houses. You have two choices for house <img src='https://latex.codecogs.com/svg.image?k' title='k' />: you can either rob house <img src='https://latex.codecogs.com/svg.image?k' title='k' />, which implies you have robbed house <img src='https://latex.codecogs.com/svg.image?k-2' title='k-2' />, or else you have robbed house <img src='https://latex.codecogs.com/svg.image?k-1' title='k-1' /> and so you do not rob <img src='https://latex.codecogs.com/svg.image?k' title='k' />. You should choose the one with higher value. Thus we have the equation
<img src='https://latex.codecogs.com/svg.image?f(k)&space;=&space;\max\{f(k-2)&space;&plus;&space;\texttt{A[k]},&space;f(k-1)\}' title='f(k)&space;=&space;\max\{f(k-2)&space;&plus;&space;\texttt{A[k]},&space;f(k-1)\}' />.

Below is a Python solution. Of course we can lower space usage from <img src='https://latex.codecogs.com/svg.image?O(n)' title='O(n)' /> to <img src='https://latex.codecogs.com/svg.image?O(1)' title='O(1)' /> by maintaining only two variables, but the purpose here is to show the DP equation in a clear way.

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        f = [nums[0], max(nums[0],nums[1])]
        for k in range(2, n):
            f.append(max(f[k-2]+nums[k], f[k-1]))
        return f[-1]
```
