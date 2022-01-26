# 650. 2 Keys Keyboard

## Some examples

Let $f(n)$ be the output, i.e. the minimum number of steps when the input is $n$. We have

> $f(1) = 0$, 
> $f(2) = 2$, 
> $f(3) = 3$, 
> $f(4) = 2 + 2 = 4$, 
> $f(5) = 5$,
> $f(6) = 2 + 3 = 5$,
> $f(7) = 7$,
> $f(8) = 2 + 2 + 2 = 6$,
> $f(9) = 3 + 3 = 6$,
> $f(10) = 5 + 2 = 7$,
> ...

We can only paste what we have lastly copied. When $n$ is a prime number, we have to copy `A` and paste it $n-1$ times. For that we need $n$ operations in total. 

When $n$ is not a prime number, it seems that any output can always be represented as the sum over prime factors of $n$. For example $6=2\cdot3$ and $f(6)=2+3=5$. So we guess, for $n = p_1\cdot p_2\cdots p_n$, where $p_1,\ldots,p_n$ are prime factors of $n$, counting multiplicity, we have 

$f(n) = p_1 + p_2 + \cdots + p_n$.

Next we prove that our conjecture is right.

## Proof

Let's recall the definition of $f(n)$: it is the minimum number of operations to turn `A` into $n$ copies of `A`, where we can only use the two operations `C` (copy) and `P` (paste). 

Notice that, any series of operations can be decomposed as several  operation groups each starting with a `C`. For example, `CPPPPCP` can turn one `A` into ten `A`s, and we can decompose it to `[CPPPP][CP]`. The operation `[CP]` multiplies the number by 2, `[CPP]` multiplies the number by 3，`[CPPP]` multiplies the number by 4 etc. So the length of the operation `[CP...]` is the multiplication factor. 

Suppose the operation to get $n$ `A`s is

`[CP..]  [CP...]  [CP...]  ...  [CP...]`

where the length of the first group is$f_1$，the length of the second group is $f_2$.......the length of the last group is$f_n$. Then the total number of operations is

$f_1 + f_2 + \cdots + f_n$

and we have $n = f_1\cdot f_2\cdots f_n$。

If $f_1$ is not prime, say it is $10$, then we can reduce the steps further. We don't have to copy `A` one time and paste it 9 times to get 10 `A`s. We can first paste 4 times, to get 5 `A`s, and then do one `[CP]` to get 10 `A`s. This costs us 7 steps, instead of 10. 

In general, if $f_1$ is not prime, $f_1 = p\cdot q, p\geq2, q\geq2$. We have

$p + q \leq pq = f_1$，

namely, instead of copy and then paste $f_1-1$ times, we can instead copy and paste $p$ times, then copy again and paste $q-1$ times. In this way we can reduce $f(n)$ from $f_1+f_2+\cdots+f_n$ to $(p+q)+f_2+\cdots+f_n$. 

The proof of the inequality is as follows:

For $p\geq2, q\geq2$，we have

$p - 1\geq1, q - 1\geq 1 \Rightarrow (p - 1)(q - 1) \geq 1 \Rightarrow p + q \leq pq$.

We have the same argument for $f_2$: if it is not a prime, then we can further reduce the steps. This way, only when all of $f_1,\ldots,f_n$ are prime numbers is their sum miminal. 

## Python Code

We proved that the output $f(n)$ is the sum of prime decompositions of $n$. So we just need to find all prime factos of $n$ and add them up.

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

When $n=20$, we can first get 10 `A`s, then copy and paste the 10 `A`s to get 20 `A`s. But how do we optimally get the 10 `A`s in the first place? For now the reader should recognize the DP equation:

$f(n) = f(m) + n/m$，

where $m$ is the largest factor of $n$ in $[1, n)$. 

Notice when $n$ is prime, we have $m=1$, $n/m=n$, and $f(n)=f(1)+n=0+n=n$.

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
