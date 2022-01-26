# 413. Arithmetic Slices

Let <img src='https://latex.codecogs.com/svg.image?f:\{0,1,\ldots,n-1\}\to\mathbb{Z}_{&plus;}' title='f:\{0,1,\ldots,n-1\}\to\mathbb{Z}_{&plus;}' /> be the value function. <img src='https://latex.codecogs.com/svg.image?f(i)' title='f(i)' /> is the number of arithmetic slices that **must** end with <img src='https://latex.codecogs.com/svg.image?i' title='i' />. For <img src='https://latex.codecogs.com/svg.image?i' title='i' />, if the condition `A[i] - A[i-1] == A[i-1] - A[i-2]` holds, then `[A[i-2], A[i-1], A[i]]` can constitute an arithmetic slice. What's more, appending `A[i]` to any slice that ends with `A[i-1]` will again give us an arithmetic slice that ends with `A[i]`. Thus, we have

<img src='https://latex.codecogs.com/svg.image?f(i)&space;=&space;f(i&space;-&space;1)&space;&plus;&space;1' title='f(i)&space;=&space;f(i&space;-&space;1)&space;&plus;&space;1' />.

The "1" in the equation refers to the slice `[A[i-2], A[i-1], A[i]]`. 

Python code is below. We initialize <img src='https://latex.codecogs.com/svg.image?f' title='f' /> with <img src='https://latex.codecogs.com/svg.image?0' title='0' />s. Note the simple fact that any arithmetic slice in `A` must have ending somewhere in the array. Each `f[i]` records the number of arithmetic slices that end with <img src='https://latex.codecogs.com/svg.image?i' title='i' />, so `f[i]`s for different `i`s record different slices. Summing the values up gives us the total number of arithmetic slices.

```python
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        f = [0] * len(A)
        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                f[i] = 1 + f[i-1]
        return sum(f)
```
