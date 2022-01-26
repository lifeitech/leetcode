# 96. Unique Binary Search Trees

Let <img src='https://latex.codecogs.com/svg.image?G(n)' title='G(n)' /> be the number of unique BSTs for nodes <img src='https://latex.codecogs.com/svg.image?1,\ldots,n' title='1,\ldots,n' />. Let <img src='https://latex.codecogs.com/svg.image?F(i,&space;n)' title='F(i,&space;n)' /> denote the number of unique BSTs for nodes <img src='https://latex.codecogs.com/svg.image?1,\ldots,n' title='1,\ldots,n' /> with <img src='https://latex.codecogs.com/svg.image?i' title='i' /> as root. We have

<img src='https://latex.codecogs.com/svg.image?G(n)&space;=&space;F(1,&space;n)&space;&plus;&space;F(2,&space;n)&space;&plus;&space;\cdots&space;&plus;&space;F(n,&space;n)' title='G(n)&space;=&space;F(1,&space;n)&space;&plus;&space;F(2,&space;n)&space;&plus;&space;\cdots&space;&plus;&space;F(n,&space;n)' />.

 By the recursive definition of BST, the left subtree and right subtree of a BST with root <img src='https://latex.codecogs.com/svg.image?i' title='i' /> are again BSTs, so we have

<img src='https://latex.codecogs.com/svg.image?F(i,&space;n)&space;=&space;G(i-1)\cdot&space;G(n-i)' title='F(i,&space;n)&space;=&space;G(i-1)\cdot&space;G(n-i)' />.

Thus the dynamic programming equation is

<img src='https://latex.codecogs.com/svg.image?G(n)&space;=&space;\sum_{i=1}^nG(i-1)\cdot&space;G(n-i)' title='G(n)&space;=&space;\sum_{i=1}^nG(i-1)\cdot&space;G(n-i)' />.

Python code:

```python
class Solution:
    def numTrees(self, n: int) -> int:
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for m in range(2, n+1):
            for i in range(1, m+1):
                G[m] += G[i-1] * G[m-i]

        return G[n]
```

Time complexity is <img src='https://latex.codecogs.com/svg.image?O(n^2)' title='O(n^2)' /> and space complexity is <img src='https://latex.codecogs.com/svg.image?O(n)' title='O(n)' />.