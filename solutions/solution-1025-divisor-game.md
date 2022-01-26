# 1025. Divisor Game

Suppose $N>1$ is odd. For any divisor $x$ of $N$, we can decompose $N$ as 

$N = x\cdot b$

for some number $0<b<N$. Since $\bar{N}=\bar{1}$, we have $\bar{N}=\bar{x}\cdot\bar{b}=\bar{1}\Rightarrow\bar{x}=\bar{1},\bar{b}=\bar{1}$. This implies $N-x = x\cdot b - x = x(b-1)$ must be even:

$\bar{N}-\bar{x} = \bar{x}(\bar{b}-\bar{1}) = \bar{1}\cdot\bar{0} = \bar{0}$.

So if Alice is given an odd number, she must return to Bob an even number. Bob can always subtract $1$ to return Alice an odd number again. So under this strategy Alice can never have the chance to get even number. Eventually, Bob will get $2$, then he can subtract $1$, return Alice $1$, and Alice will lose the game. Similarly, if Alice is given an even number, then she can always return Bob an odd number. In this scenario Alice will eventually have $2$ and Bob will eventually have $1$, so it is Bob that will lose the game.

In summary, if Alice gets an odd number, she loses; if she gets an even number, she wins.

Python code

```python
class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0
```
