# 338. Counting Bits

First we observe that the binary representation of any even number must have a <img src='https://latex.codecogs.com/svg.image?0' title='0' /> in the end, like <img src='https://latex.codecogs.com/svg.image?2=10' title='2=10' />, <img src='https://latex.codecogs.com/svg.image?4=100' title='4=100' />, <img src='https://latex.codecogs.com/svg.image?6=110' title='6=110' />, <img src='https://latex.codecogs.com/svg.image?8=1000' title='8=1000' /> etc. This is because the binary representation of <img src='https://latex.codecogs.com/svg.image?2' title='2' /> is <img src='https://latex.codecogs.com/svg.image?10' title='10' />, and all even numbers are divisible by <img src='https://latex.codecogs.com/svg.image?2' title='2' />. Similarly, since all odd numbers are not divisible by <img src='https://latex.codecogs.com/svg.image?2' title='2' />, they always have <img src='https://latex.codecogs.com/svg.image?1' title='1' /> in the end of their binary representations.

Let <img src='https://latex.codecogs.com/svg.image?f(i)' title='f(i)' /> be the number of ones in binary number <img src='https://latex.codecogs.com/svg.image?i' title='i' />. An odd number <img src='https://latex.codecogs.com/svg.image?i' title='i' /> is always equal to its previous even number <img src='https://latex.codecogs.com/svg.image?i-1' title='i-1' /> plus one, add from above we can deduce that the number of ones in <img src='https://latex.codecogs.com/svg.image?i' title='i' /> is equal to <img src='https://latex.codecogs.com/svg.image?f(i-1)&plus;1' title='f(i-1)&plus;1' />. If <img src='https://latex.codecogs.com/svg.image?i' title='i' /> is an even number, then dividing it by <img src='https://latex.codecogs.com/svg.image?2=10' title='2=10' /> will remove the <img src='https://latex.codecogs.com/svg.image?0' title='0' /> in the end but will not alter the number of ones in <img src='https://latex.codecogs.com/svg.image?i' title='i' />, so we have <img src='https://latex.codecogs.com/svg.image?f(i)&space;=&space;f(i/2)' title='f(i)&space;=&space;f(i/2)' />. In summary,

<img src='https://latex.codecogs.com/svg.image?f(i)&space;=&space;\begin{cases}f(i-1)&space;&plus;&space;1&space;&&space;\text{&space;if&space;}i\text{&space;is&space;odd,}\\&space;f(i/2)&space;&&space;\text{&space;if&space;}i\text{&space;is&space;even.}&space;\end{cases}' title='f(i)&space;=&space;\begin{cases}f(i-1)&space;&plus;&space;1&space;&&space;\text{&space;if&space;}i\text{&space;is&space;odd,}\\&space;f(i/2)&space;&&space;\text{&space;if&space;}i\text{&space;is&space;even.}&space;\end{cases}' />

Python code:

```python
class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0]*(num+1)
        for i in range(1, num+1):
            if i % 2 == 1:
                result[i] = result[i-1] + 1
            else:
                result[i] = result[i//2]
        return result
```
