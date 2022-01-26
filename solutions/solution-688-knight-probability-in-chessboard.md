# 688. Knight Probability in Chessboard

Let <img src='https://latex.codecogs.com/svg.image?p(r,&space;c,&space;k)' title='p(r,&space;c,&space;k)' /> be the probability that the knight _still_ remains on the chessboard _after it starts at <img src='https://latex.codecogs.com/svg.image?(r,&space;c)' title='(r,&space;c)' /> and moves <img src='https://latex.codecogs.com/svg.image?k' title='k' /> steps_. The 8 possible moves are

* <img src='https://latex.codecogs.com/svg.image?(&plus;2,&space;&plus;1)' title='(&plus;2,&space;&plus;1)' />;
* <img src='https://latex.codecogs.com/svg.image?(&plus;2,&space;-1)' title='(&plus;2,&space;-1)' />;
* <img src='https://latex.codecogs.com/svg.image?(-2,&space;&plus;1)' title='(-2,&space;&plus;1)' />;
* <img src='https://latex.codecogs.com/svg.image?(-2,&space;-1)' title='(-2,&space;-1)' />;
* <img src='https://latex.codecogs.com/svg.image?(&plus;1,&space;&plus;2)' title='(&plus;1,&space;&plus;2)' />;
* <img src='https://latex.codecogs.com/svg.image?(&plus;1,&space;-2)' title='(&plus;1,&space;-2)' />;
* <img src='https://latex.codecogs.com/svg.image?(-1,&space;-2)' title='(-1,&space;-2)' />;
* <img src='https://latex.codecogs.com/svg.image?(-1,&space;&plus;2)' title='(-1,&space;&plus;2)' />.

In the first step, it can take one of the 8 moves. If it takes the first move <img src='https://latex.codecogs.com/svg.image?(&plus;2,&space;&plus;1)' title='(&plus;2,&space;&plus;1)' />, then we come to the point <img src='https://latex.codecogs.com/svg.image?(r&plus;2,&space;c&plus;1)' title='(r&plus;2,&space;c&plus;1)' />. The probability <img src='https://latex.codecogs.com/svg.image?p(r,&space;c,&space;k)' title='p(r,&space;c,&space;k)' /> is then <img src='https://latex.codecogs.com/svg.image?p(r&plus;2,&space;c&plus;1,&space;k-1)' title='p(r&plus;2,&space;c&plus;1,&space;k-1)' />, i.e. the probability that the knight will remain on the board after <img src='https://latex.codecogs.com/svg.image?k-1' title='k-1' /> moves, starting at <img src='https://latex.codecogs.com/svg.image?(r&plus;2,&space;c&plus;1)' title='(r&plus;2,&space;c&plus;1)' />. Similarly, if it takes the second move <img src='https://latex.codecogs.com/svg.image?(&plus;2,&space;-1)' title='(&plus;2,&space;-1)' />, then the probability <img src='https://latex.codecogs.com/svg.image?p(r,&space;c,&space;k)' title='p(r,&space;c,&space;k)' /> would become <img src='https://latex.codecogs.com/svg.image?p(r&plus;2,&space;c-1,&space;k-1)' title='p(r&plus;2,&space;c-1,&space;k-1)' />. Of course we don't know in advance which move it will take. Each direction is taken with equal probability (<img src='https://latex.codecogs.com/svg.image?1/8' title='1/8' />), so we should take the expectation:

<img src='https://latex.codecogs.com/svg.image?\displaystyle&space;p(r,&space;c,&space;k)&space;=&space;p(r&plus;2,&space;c&plus;1,&space;k-1)\cdot\frac{1}{8}&space;&plus;&space;p(r&plus;2,&space;c-1,&space;k-1)\cdot\frac{1}{8}&space;&plus;&space;\cdots&space;&plus;&space;p(r-1,&space;c&plus;2,&space;k-1)\cdot\frac{1}{8}' title='\displaystyle&space;p(r,&space;c,&space;k)&space;=&space;p(r&plus;2,&space;c&plus;1,&space;k-1)\cdot\frac{1}{8}&space;&plus;&space;p(r&plus;2,&space;c-1,&space;k-1)\cdot\frac{1}{8}&space;&plus;&space;\cdots&space;&plus;&space;p(r-1,&space;c&plus;2,&space;k-1)\cdot\frac{1}{8}' />.

The above is the DP transition equation. The final answer is

<img src='https://latex.codecogs.com/svg.image?\displaystyle&space;\sum_{r=0}^{N-1}\sum_{c=0}^{N-1}p(r,&space;c,&space;K)' title='\displaystyle&space;\sum_{r=0}^{N-1}\sum_{c=0}^{N-1}p(r,&space;c,&space;K)' />.

Python code below. Note that <img src='https://latex.codecogs.com/svg.image?p(\cdot,&space;\cdot,&space;k)' title='p(\cdot,&space;\cdot,&space;k)' /> only depends on <img src='https://latex.codecogs.com/svg.image?p(\cdot,&space;\cdot,&space;k-1)' title='p(\cdot,&space;\cdot,&space;k-1)' />, so we do not maintain the third variable <img src='https://latex.codecogs.com/svg.image?k' title='k' /> in the program. 

```python
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        p = {(r, c): 1}
        for _ in range(K):
            p = {(r, c): sum(p.get((r+i, c+j), 0) + p.get((r+j, c+i), 0) for i in (1, -1) for j in (2, -2)) / 8 
                 for r in range(N) for c in range(N)}

        return sum(p.values())
```