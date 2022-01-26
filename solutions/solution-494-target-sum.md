# 494. Target Sum

Let <img src='https://latex.codecogs.com/svg.image?x' title='x' /> be the sum of positive terms, and let <img src='https://latex.codecogs.com/svg.image?y' title='y' /> be the sum of the negative terms. We want
<img src='https://latex.codecogs.com/svg.image?\displaystyle&space;\begin{cases}x&space;-&space;y&space;=&space;S\\&space;x&space;&plus;&space;y&space;=&space;\texttt{sum(nums)}\end{cases}&space;\Rightarrow&space;2x&space;=&space;S&space;&plus;&space;\texttt{sum(nums)}&space;\Rightarrow&space;x&space;=&space;\frac{S&space;&plus;&space;\texttt{sum(nums)}}{2}.' title='\displaystyle&space;\begin{cases}x&space;-&space;y&space;=&space;S\\&space;x&space;&plus;&space;y&space;=&space;\texttt{sum(nums)}\end{cases}&space;\Rightarrow&space;2x&space;=&space;S&space;&plus;&space;\texttt{sum(nums)}&space;\Rightarrow&space;x&space;=&space;\frac{S&space;&plus;&space;\texttt{sum(nums)}}{2}.' />

The problem then becomes: select some elements from the input array so that they sum to target `(sum(nums) + S) // 2`. Return the count of all such possible selections.

Let <img src='https://latex.codecogs.com/svg.image?f(i,&space;j)' title='f(i,&space;j)' /> be the # of ways for input `nums[:i+1]` and target `j`. We can either use `nums[i]`, or not use it. If we do not use `nums[i]`, then there are <img src='https://latex.codecogs.com/svg.image?f(i&space;-&space;1,&space;j)' title='f(i&space;-&space;1,&space;j)' /> ways of summing to the target `j`. On the other hand, how many ways are there if `nums[i]` must be used? This is equal to the # of ways of summing up to `j - nums[i]` in the array `nums[:i]`, i.e. <img src='https://latex.codecogs.com/svg.image?f(i&space;-&space;1,&space;j&space;-&space;\texttt{nums[i]})' title='f(i&space;-&space;1,&space;j&space;-&space;\texttt{nums[i]})' />. Thus, <img src='https://latex.codecogs.com/svg.image?f(i,&space;j)' title='f(i,&space;j)' /> is equal to the sum of the two counts:

<img src='https://latex.codecogs.com/svg.image?f(i,&space;j)&space;=&space;f(i&space;-&space;1,&space;j)&space;&plus;&space;f(i&space;-&space;1,&space;j&space;-&space;\texttt{nums[i]})' title='f(i,&space;j)&space;=&space;f(i&space;-&space;1,&space;j)&space;&plus;&space;f(i&space;-&space;1,&space;j&space;-&space;\texttt{nums[i]})' />.

We can then write down the program by following the DP equation. See below. There is one way of summing `nums[0]` to <img src='https://latex.codecogs.com/svg.image?0' title='0' />, namely not pick the element, so we initialize `f[0]` as <img src='https://latex.codecogs.com/svg.image?1' title='1' />. The terms involving `i` on the right hand side of the equation are the same (<img src='https://latex.codecogs.com/svg.image?i-1' title='i-1' />), so we drop variable <img src='https://latex.codecogs.com/svg.image?i' title='i' /> and use one-dimensional array to store values of <img src='https://latex.codecogs.com/svg.image?f' title='f' />. 

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if sum(nums) < S or (sum(nums) + S) % 2 == 1: return 0
        target = (sum(nums) + S) // 2
        f = [1] + [0 for _ in range(target)]
        for i in range(len(nums)):
            for j in range(target,nums[i] - 1, -1):
                f[j]  = f[j] +  f[j - nums[i]]
        return f[target]
```

Note that the equation as well as the code are almost the same to that in the [partition equal subset sum](https://leetcode-cn.com/problems/partition-equal-subset-sum/) problem. I copy the DP equation for the partition equal subset sum problem here:

<img src='https://latex.codecogs.com/svg.image?f(i,&space;j)&space;=&space;f(i&space;-&space;1,&space;j)&space;\vee&space;f(i&space;-&space;1,&space;j&space;-&space;\texttt{nums[i]})' title='f(i,&space;j)&space;=&space;f(i&space;-&space;1,&space;j)&space;\vee&space;f(i&space;-&space;1,&space;j&space;-&space;\texttt{nums[i]})' />.

We can see that <img src='https://latex.codecogs.com/svg.image?&plus;' title='&plus;' /> corresponds to <img src='https://latex.codecogs.com/svg.image?\vee' title='\vee' />. One function is numerical, the other has binary output. They have the same structure because the two problems are essentially the same 0-1 knapsack problem.