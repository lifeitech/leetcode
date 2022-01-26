# 258. n mod 9

The  answer is <img src='https://latex.codecogs.com/svg.image?n\bmod&space;9' title='n\bmod&space;9' />, as explained [here](https://en.wikipedia.org/wiki/Digital_root). The reason is simple, all is because <img src='https://latex.codecogs.com/svg.image?10=1&space;\bmod&space;9' title='10=1&space;\bmod&space;9' /> and so <img src='https://latex.codecogs.com/svg.image?10^k&space;=&space;1\bmod&space;9' title='10^k&space;=&space;1\bmod&space;9' /> as well. Let <img src='https://latex.codecogs.com/svg.image?f(n)' title='f(n)' /> denote the function we want to compute. Let 

<img src='https://latex.codecogs.com/svg.image?n&space;=&space;a_k\cdot&space;10^k&space;&plus;&space;a_{k-1}\cdot&space;10^{k-1}&space;&plus;&space;\cdots&space;&plus;&space;a_0' title='n&space;=&space;a_k\cdot&space;10^k&space;&plus;&space;a_{k-1}\cdot&space;10^{k-1}&space;&plus;&space;\cdots&space;&plus;&space;a_0' />.

Take modulo <img src='https://latex.codecogs.com/svg.image?9' title='9' /> we find

<img src='https://latex.codecogs.com/svg.image?\bar{n}&space;=&space;\overline{a_k&space;&plus;&space;a_{k-1}&space;&plus;&space;\cdots&space;&plus;&space;a_0}' title='\bar{n}&space;=&space;\overline{a_k&space;&plus;&space;a_{k-1}&space;&plus;&space;\cdots&space;&plus;&space;a_0}' />.

If the sum of <img src='https://latex.codecogs.com/svg.image?a_k,\ldots,a_0' title='a_k,\ldots,a_0' /> is smaller than <img src='https://latex.codecogs.com/svg.image?10' title='10' />, then we are done. The numerical result is equal to <img src='https://latex.codecogs.com/svg.image?f(n)' title='f(n)' />. If it is larger than or eqiual to <img src='https://latex.codecogs.com/svg.image?10' title='10' />, then we can express the number as, say

<img src='https://latex.codecogs.com/svg.image?b_j&space;\cdot&space;10^j&space;&plus;&space;\cdots&space;&plus;&space;b_0' title='b_j&space;\cdot&space;10^j&space;&plus;&space;\cdots&space;&plus;&space;b_0' />

so taking modulo <img src='https://latex.codecogs.com/svg.image?9' title='9' /> we will have <img src='https://latex.codecogs.com/svg.image?\overline{b_j&plus;\cdots&plus;b_0}' title='\overline{b_j&plus;\cdots&plus;b_0}' />. If the sum of <img src='https://latex.codecogs.com/svg.image?b_j,\ldots,b_0' title='b_j,\ldots,b_0' /> is smaller than <img src='https://latex.codecogs.com/svg.image?10' title='10' /> we are done; otherwise we continue to apply the modulo operation. This is exactly what we wanted: sum digits recursively until a single number is left. Thus the number we obtained from <img src='https://latex.codecogs.com/svg.image?\bar{n}' title='\bar{n}' /> (i.e. <img src='https://latex.codecogs.com/svg.image?n\bmod&space;9' title='n\bmod&space;9' />) should be <img src='https://latex.codecogs.com/svg.image?f(n)' title='f(n)' />. 

Lastly, for <img src='https://latex.codecogs.com/svg.image?n=0' title='n=0' /> we should return <img src='https://latex.codecogs.com/svg.image?0' title='0' />. If <img src='https://latex.codecogs.com/svg.image?n' title='n' /> is nonzero and <img src='https://latex.codecogs.com/svg.image?\bar{n}&space;=&space;\bar{0}' title='\bar{n}&space;=&space;\bar{0}' /> (i.e. it is divisible by <img src='https://latex.codecogs.com/svg.image?9' title='9' />), then <img src='https://latex.codecogs.com/svg.image?f(n)' title='f(n)' /> shall be set to <img src='https://latex.codecogs.com/svg.image?9' title='9' />.

```python
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9
```
