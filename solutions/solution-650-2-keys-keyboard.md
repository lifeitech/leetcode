# 650. 2 Keys Keyboard

## Some examples

Let <img src='https://latex.codecogs.com/svg.image?f(n)' title='f(n)' /> be the output, i.e. the minimum number of steps when the input is <img src='https://latex.codecogs.com/svg.image?n' title='n' />. We have

> <img src='https://latex.codecogs.com/svg.image?f(1)&space;=&space;0' title='f(1)&space;=&space;0' />, 
> <img src='https://latex.codecogs.com/svg.image?f(2)&space;=&space;2' title='f(2)&space;=&space;2' />, 
> <img src='https://latex.codecogs.com/svg.image?f(3)&space;=&space;3' title='f(3)&space;=&space;3' />, 
> <img src='https://latex.codecogs.com/svg.image?f(4)&space;=&space;2&space;&plus;&space;2&space;=&space;4' title='f(4)&space;=&space;2&space;&plus;&space;2&space;=&space;4' />, 
> <img src='https://latex.codecogs.com/svg.image?f(5)&space;=&space;5' title='f(5)&space;=&space;5' />,
> <img src='https://latex.codecogs.com/svg.image?f(6)&space;=&space;2&space;&plus;&space;3&space;=&space;5' title='f(6)&space;=&space;2&space;&plus;&space;3&space;=&space;5' />,
> <img src='https://latex.codecogs.com/svg.image?f(7)&space;=&space;7' title='f(7)&space;=&space;7' />,
> <img src='https://latex.codecogs.com/svg.image?f(8)&space;=&space;2&space;&plus;&space;2&space;&plus;&space;2&space;=&space;6' title='f(8)&space;=&space;2&space;&plus;&space;2&space;&plus;&space;2&space;=&space;6' />,
> <img src='https://latex.codecogs.com/svg.image?f(9)&space;=&space;3&space;&plus;&space;3&space;=&space;6' title='f(9)&space;=&space;3&space;&plus;&space;3&space;=&space;6' />,
> <img src='https://latex.codecogs.com/svg.image?f(10)&space;=&space;5&space;&plus;&space;2&space;=&space;7' title='f(10)&space;=&space;5&space;&plus;&space;2&space;=&space;7' />,
> ...

We can only paste what we have lastly copied. When <img src='https://latex.codecogs.com/svg.image?n' title='n' /> is a prime number, we have to copy `A` and paste it <img src='https://latex.codecogs.com/svg.image?n-1' title='n-1' /> times. For that we need <img src='https://latex.codecogs.com/svg.image?n' title='n' /> operations in total. 

When <img src='https://latex.codecogs.com/svg.image?n' title='n' /> is not a prime number, it seems that any output can always be represented as the sum over prime factors of <img src='https://latex.codecogs.com/svg.image?n' title='n' />. For example <img src='https://latex.codecogs.com/svg.image?6=2\cdot3' title='6=2\cdot3' /> and <img src='https://latex.codecogs.com/svg.image?f(6)=2&plus;3=5' title='f(6)=2&plus;3=5' />. So we guess, for <img src='https://latex.codecogs.com/svg.image?n&space;=&space;p_1\cdot&space;p_2\cdots&space;p_n' title='n&space;=&space;p_1\cdot&space;p_2\cdots&space;p_n' />, where <img src='https://latex.codecogs.com/svg.image?p_1,\ldots,p_n' title='p_1,\ldots,p_n' /> are prime factors of <img src='https://latex.codecogs.com/svg.image?n' title='n' />, counting multiplicity, we have 

<img src='https://latex.codecogs.com/svg.image?f(n)&space;=&space;p_1&space;&plus;&space;p_2&space;&plus;&space;\cdots&space;&plus;&space;p_n' title='f(n)&space;=&space;p_1&space;&plus;&space;p_2&space;&plus;&space;\cdots&space;&plus;&space;p_n' />.

Next we prove that our conjecture is right.

## Proof

Let's recall the definition of <img src='https://latex.codecogs.com/svg.image?f(n)' title='f(n)' />: it is the minimum number of operations to turn `A` into <img src='https://latex.codecogs.com/svg.image?n' title='n' /> copies of `A`, where we can only use the two operations `C` (copy) and `P` (paste). 

Notice that, any series of operations can be decomposed as several  operation groups each starting with a `C`. For example, `CPPPPCP` can turn one `A` into ten `A`s, and we can decompose it to `[CPPPP][CP]`. The operation `[CP]` multiplies the number by 2, `[CPP]` multiplies the number by 3，`[CPPP]` multiplies the number by 4 etc. So the length of the operation `[CP...]` is the multiplication factor. 

Suppose the operation to get <img src='https://latex.codecogs.com/svg.image?n' title='n' /> `A`s is

`[CP..]  [CP...]  [CP...]  ...  [CP...]`

where the length of the first group is<img src='https://latex.codecogs.com/svg.image?f_1' title='f_1' />，the length of the second group is <img src='https://latex.codecogs.com/svg.image?f_2' title='f_2' />.......the length of the last group is<img src='https://latex.codecogs.com/svg.image?f_n' title='f_n' />. Then the total number of operations is

<img src='https://latex.codecogs.com/svg.image?f_1&space;&plus;&space;f_2&space;&plus;&space;\cdots&space;&plus;&space;f_n' title='f_1&space;&plus;&space;f_2&space;&plus;&space;\cdots&space;&plus;&space;f_n' />

and we have <img src='https://latex.codecogs.com/svg.image?n&space;=&space;f_1\cdot&space;f_2\cdots&space;f_n' title='n&space;=&space;f_1\cdot&space;f_2\cdots&space;f_n' />。

If <img src='https://latex.codecogs.com/svg.image?f_1' title='f_1' /> is not prime, say it is <img src='https://latex.codecogs.com/svg.image?10' title='10' />, then we can reduce the steps further. We don't have to copy `A` one time and paste it 9 times to get 10 `A`s. We can first paste 4 times, to get 5 `A`s, and then do one `[CP]` to get 10 `A`s. This costs us 7 steps, instead of 10. 

In general, if <img src='https://latex.codecogs.com/svg.image?f_1' title='f_1' /> is not prime, <img src='https://latex.codecogs.com/svg.image?f_1&space;=&space;p\cdot&space;q,&space;p\geq2,&space;q\geq2' title='f_1&space;=&space;p\cdot&space;q,&space;p\geq2,&space;q\geq2' />. We have

<img src='https://latex.codecogs.com/svg.image?p&space;&plus;&space;q&space;\leq&space;pq&space;=&space;f_1' title='p&space;&plus;&space;q&space;\leq&space;pq&space;=&space;f_1' />，

namely, instead of copy and then paste <img src='https://latex.codecogs.com/svg.image?f_1-1' title='f_1-1' /> times, we can instead copy and paste <img src='https://latex.codecogs.com/svg.image?p' title='p' /> times, then copy again and paste <img src='https://latex.codecogs.com/svg.image?q-1' title='q-1' /> times. In this way we can reduce <img src='https://latex.codecogs.com/svg.image?f(n)' title='f(n)' /> from <img src='https://latex.codecogs.com/svg.image?f_1&plus;f_2&plus;\cdots&plus;f_n' title='f_1&plus;f_2&plus;\cdots&plus;f_n' /> to <img src='https://latex.codecogs.com/svg.image?(p&plus;q)&plus;f_2&plus;\cdots&plus;f_n' title='(p&plus;q)&plus;f_2&plus;\cdots&plus;f_n' />. 

The proof of the inequality is as follows:

For <img src='https://latex.codecogs.com/svg.image?p\geq2,&space;q\geq2' title='p\geq2,&space;q\geq2' />，we have

<img src='https://latex.codecogs.com/svg.image?p&space;-&space;1\geq1,&space;q&space;-&space;1\geq&space;1&space;\Rightarrow&space;(p&space;-&space;1)(q&space;-&space;1)&space;\geq&space;1&space;\Rightarrow&space;p&space;&plus;&space;q&space;\leq&space;pq' title='p&space;-&space;1\geq1,&space;q&space;-&space;1\geq&space;1&space;\Rightarrow&space;(p&space;-&space;1)(q&space;-&space;1)&space;\geq&space;1&space;\Rightarrow&space;p&space;&plus;&space;q&space;\leq&space;pq' />.

We have the same argument for <img src='https://latex.codecogs.com/svg.image?f_2' title='f_2' />: if it is not a prime, then we can further reduce the steps. This way, only when all of <img src='https://latex.codecogs.com/svg.image?f_1,\ldots,f_n' title='f_1,\ldots,f_n' /> are prime numbers is their sum miminal. 

## Python Code

We proved that the output <img src='https://latex.codecogs.com/svg.image?f(n)' title='f(n)' /> is the sum of prime decompositions of <img src='https://latex.codecogs.com/svg.image?n' title='n' />. So we just need to find all prime factos of <img src='https://latex.codecogs.com/svg.image?n' title='n' /> and add them up.

```python
class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans
```

## DP Equation

When <img src='https://latex.codecogs.com/svg.image?n=20' title='n=20' />, we can first get 10 `A`s, then copy and paste the 10 `A`s to get 20 `A`s. But how do we optimally get the 10 `A`s in the first place? For now the reader should recognize the DP equation:

<img src='https://latex.codecogs.com/svg.image?f(n)&space;=&space;f(m)&space;&plus;&space;n/m' title='f(n)&space;=&space;f(m)&space;&plus;&space;n/m' />，

where <img src='https://latex.codecogs.com/svg.image?m' title='m' /> is the largest factor of <img src='https://latex.codecogs.com/svg.image?n' title='n' /> in <img src='https://latex.codecogs.com/svg.image?[1,&space;n)' title='[1,&space;n)' />. 

Notice when <img src='https://latex.codecogs.com/svg.image?n' title='n' /> is prime, we have <img src='https://latex.codecogs.com/svg.image?m=1' title='m=1' />, <img src='https://latex.codecogs.com/svg.image?n/m=n' title='n/m=n' />, and <img src='https://latex.codecogs.com/svg.image?f(n)=f(1)&plus;n=0&plus;n=n' title='f(n)=f(1)&plus;n=0&plus;n=n' />.

Below is the Python code that implements the DP equation. Notice the `break` statement.

```python
class Solution:
    def minSteps(self, n: int) -> int:
        f = [0 for i in range(n+1)]
        for m in range(2, n+1):
            for i in range(m-1, 0, -1):
                if m % i == 0:
                    f[m] = f[i] + m//i
                    break
        return f[n]
```
