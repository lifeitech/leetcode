# 813. Largest Sum of Averages

Let <img src='https://latex.codecogs.com/svg.image?f(i,&space;k)' title='f(i,&space;k)' /> be the value (output) function for array `A[i:]` with at most <img src='https://latex.codecogs.com/svg.image?k' title='k' /> groups. Like the value function in the [Partition Equal Subset Sum Problem](https://leetcode-cn.com/problems/partition-equal-subset-sum/), the two variables of the function are _heterogeneous_. They represent very different (and unrelated) things. This is unlike the [Minimum Falling Path Problem](https://leetcode-cn.com/problems/minimum-falling-path-sum/) where <img src='https://latex.codecogs.com/svg.image?i' title='i' /> and <img src='https://latex.codecogs.com/svg.image?j' title='j' /> in the value function <img src='https://latex.codecogs.com/svg.image?f(i,&space;j)' title='f(i,&space;j)' /> are all coordinates. 

The transition equation is

<img src='https://latex.codecogs.com/svg.image?f(i,&space;k)&space;=&space;\max\left\{\bar{A}_{i:N},\,\,&space;\max_{j>i}\{\bar{A}_{i:j}&space;&plus;&space;f(j,&space;k-1)\}&space;\right\}' title='f(i,&space;k)&space;=&space;\max\left\{\bar{A}_{i:N},\,\,&space;\max_{j>i}\{\bar{A}_{i:j}&space;&plus;&space;f(j,&space;k-1)\}&space;\right\}' />,

where <img src='https://latex.codecogs.com/svg.image?A_{i:j}' title='A_{i:j}' /> means the array `A[i:j+1]`, and <img src='https://latex.codecogs.com/svg.image?\bar{A}' title='\bar{A}' /> means the average value over the array `A`.

To determine the largest value for the array `A[i:]`, we look at every point `j` in `A[i:]`. We can choose to not split the array, the value of which is <img src='https://latex.codecogs.com/svg.image?\bar{A}_{i:N}' title='\bar{A}_{i:N}' />. Or we can split at any `j`. After the split, the value is the the mean over `A[i:j+1]`, plus the optimal value over `A[j:]` with at most <img src='https://latex.codecogs.com/svg.image?k-1' title='k-1' /> groups. The optimal value <img src='https://latex.codecogs.com/svg.image?f(i,&space;k)' title='f(i,&space;k)' /> should be the maximal one among those choices. This is a little-bit similar to the rod-cutting problem, where we choose the cut point.

Python code below.

```python
class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        S= [0]
        for a_i in A:
            S.append(S[-1] + a_i)
        def average(i, j):
            return (S[j] - S[i]) / float(j - i)

        N = len(A)
        f = [average(i, N) for i in range(N)]
        for k in range(K-1):
            for i in range(N):
                for j in range(i+1, N):
                    f[i] = max(f[i], average(i, j) + f[j])
        return f[0]
```
