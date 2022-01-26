# 416. Partition Equal Subset Sum

 This problem is, whether we can select some elements from the array so that their sum is `sum(nums) / 2`. This is a 0-1 knapsack problem. Let $f(i, j)$ be the value function that returns if there are elements in `nums[:i+1]` that can sum to `j`. The range of the function is $\{T, F\}$, namely true and false. The DP equation is

$f(i, j) = f(i - 1, j) \vee f(i - 1, j - \texttt{nums[i]})$.

If we don't use `nums[i]`, then $f(i, j)$ is equal to $f(i-1, j)$; if we use `nums[i]`, then the question reduces to whether there are elements in `nums[:i]` that can sum to $j-\texttt{nums[i]}$. As long as any of the two is true, $f(i, j)$ should be true as well.

We can then write down our program based on this DP equation. Since there is $i-1$ in both terms in the right-hide side, we can drop this index and use instead a **for** loop to iterate. There is also no need to go beyond `0` when updating `f[j]`, so we can stop when we are at `j-nums[i] = 0`. 

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1: return 0
        target = s // 2
        f = [True] + [False for _ in range(target)]
        for i in range(len(nums)):
            for j in range(target,nums[i] - 1, -1):
                f[j]  = f[j] or  f[j - nums[i]]
        return f[target]
```

Note that this problem is very similar to the [target sum](https://leetcode-cn.com/problems/target-sum/submissions/) problem. 