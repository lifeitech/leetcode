# 813. Largest Sum of Averages

Let $f(i, k)$ be the value (output) function for array `A[i:]` with at most $k$ groups. Like the value function in the [Partition Equal Subset Sum Problem](https://leetcode-cn.com/problems/partition-equal-subset-sum/), the two variables of the function are _heterogeneous_. They represent very different (and unrelated) things. This is unlike the [Minimum Falling Path Problem](https://leetcode-cn.com/problems/minimum-falling-path-sum/) where $i$ and $j$ in the value function $f(i, j)$ are all coordinates. 

The transition equation is

$f(i, k) = \max\left\{\bar{A}_{i:N},\,\, \max_{j>i}\{\bar{A}_{i:j} + f(j, k-1)\} \right\}$,

where $A_{i:j}$ means the array `A[i:j+1]`, and $\bar{A}$ means the average value over the array `A`.

To determine the largest value for the array `A[i:]`, we look at every point `j` in `A[i:]`. We can choose to not split the array, the value of which is $\bar{A}_{i:N}$. Or we can split at any `j`. After the split, the value is the the mean over `A[i:j+1]`, plus the optimal value over `A[j:]` with at most $k-1$ groups. The optimal value $f(i, k)$ should be the maximal one among those choices. This is a little-bit similar to the rod-cutting problem, where we choose the cut point.

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
