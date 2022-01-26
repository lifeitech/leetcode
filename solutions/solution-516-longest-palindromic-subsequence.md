# 516. Longest Palindromic Subsequence

Let <img src='https://latex.codecogs.com/svg.image?f(i,&space;j)' title='f(i,&space;j)' /> be the length of the longest palindromic subsequence for the substring `s[i:j+1]`. Then we have

<img src='https://latex.codecogs.com/svg.image?f(i,&space;j)&space;=&space;\begin{cases}&space;2&space;&plus;&space;f(i&plus;1,&space;j-1)&space;&&space;\text{&space;if&space;}s[i]&space;=&space;s[j];\\&space;\max\{f(i&plus;1,&space;j),&space;f(i,&space;j-1)&space;&space;\}&space;&&space;\text{&space;if&space;}s[i]\neq&space;s[j].\\\end{cases}' title='f(i,&space;j)&space;=&space;\begin{cases}&space;2&space;&plus;&space;f(i&plus;1,&space;j-1)&space;&&space;\text{&space;if&space;}s[i]&space;=&space;s[j];\\&space;\max\{f(i&plus;1,&space;j),&space;f(i,&space;j-1)&space;&space;\}&space;&&space;\text{&space;if&space;}s[i]\neq&space;s[j].\\\end{cases}' />

See below for the Python code. We have to judge whether the input `s` is a palindromic string first, otherwise we will get timout error.

```python
import numpy as np

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        if s == s[::-1]:
            return len(s)

        n = len(s)
        if  n == 0:
            return 0
        f = np.zeros(shape=(n,n), dtype=int)
        for i in range(n-1, -1, -1):
            f[i, i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    f[i, j] = 2 + f[i+1, j - 1]
                else:
                    f[i, j] = max(f[i+1, j], f[i, j - 1])
        return f[0, n-1]
```