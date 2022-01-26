# 1025. Divisor Game

Suppose <img src='https://latex.codecogs.com/svg.image?N>1' title='N>1' /> is odd. For any divisor <img src='https://latex.codecogs.com/svg.image?x' title='x' /> of <img src='https://latex.codecogs.com/svg.image?N' title='N' />, we can decompose <img src='https://latex.codecogs.com/svg.image?N' title='N' /> as 

<img src='https://latex.codecogs.com/svg.image?N&space;=&space;x\cdot&space;b' title='N&space;=&space;x\cdot&space;b' />

for some number <img src='https://latex.codecogs.com/svg.image?0<b<N' title='0<b<N' />. Since <img src='https://latex.codecogs.com/svg.image?\bar{N}=\bar{1}' title='\bar{N}=\bar{1}' />, we have <img src='https://latex.codecogs.com/svg.image?\bar{N}=\bar{x}\cdot\bar{b}=\bar{1}\Rightarrow\bar{x}=\bar{1},\bar{b}=\bar{1}' title='\bar{N}=\bar{x}\cdot\bar{b}=\bar{1}\Rightarrow\bar{x}=\bar{1},\bar{b}=\bar{1}' />. This implies <img src='https://latex.codecogs.com/svg.image?N-x&space;=&space;x\cdot&space;b&space;-&space;x&space;=&space;x(b-1)' title='N-x&space;=&space;x\cdot&space;b&space;-&space;x&space;=&space;x(b-1)' /> must be even:

<img src='https://latex.codecogs.com/svg.image?\bar{N}-\bar{x}&space;=&space;\bar{x}(\bar{b}-\bar{1})&space;=&space;\bar{1}\cdot\bar{0}&space;=&space;\bar{0}' title='\bar{N}-\bar{x}&space;=&space;\bar{x}(\bar{b}-\bar{1})&space;=&space;\bar{1}\cdot\bar{0}&space;=&space;\bar{0}' />.

So if Alice is given an odd number, she must return to Bob an even number. Bob can always subtract <img src='https://latex.codecogs.com/svg.image?1' title='1' /> to return Alice an odd number again. So under this strategy Alice can never have the chance to get even number. Eventually, Bob will get <img src='https://latex.codecogs.com/svg.image?2' title='2' />, then he can subtract <img src='https://latex.codecogs.com/svg.image?1' title='1' />, return Alice <img src='https://latex.codecogs.com/svg.image?1' title='1' />, and Alice will lose the game. Similarly, if Alice is given an even number, then she can always return Bob an odd number. In this scenario Alice will eventually have <img src='https://latex.codecogs.com/svg.image?2' title='2' /> and Bob will eventually have <img src='https://latex.codecogs.com/svg.image?1' title='1' />, so it is Bob that will lose the game.

In summary, if Alice gets an odd number, she loses; if she gets an even number, she wins.

Python code

```python
class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0
```
