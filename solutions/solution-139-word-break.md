# 139. Word Break

**Notation**  In the text below, notation like `a[i:j]` means the subarray from `a[i]` to `a[j]` _inclusive_. 

## Rod Cutting

This word break problem is very similar to the rod-cutting problem, so let's first review the problem briefly. Let <img src='https://latex.codecogs.com/svg.image?f(i)' title='f(i)' /> denote the value function for the rod `r[:i]`. We want to calculate <img src='https://latex.codecogs.com/svg.image?f(n)' title='f(n)' />, where <img src='https://latex.codecogs.com/svg.image?n' title='n' /> is the size of the input. For any cut point <img src='https://latex.codecogs.com/svg.image?j' title='j' /> we choose, the rod would be divided into two parts: a part that has value <img src='https://latex.codecogs.com/svg.image?p_j' title='p_j' />, the price for a piece of length <img src='https://latex.codecogs.com/svg.image?j' title='j' />, and a remaining part which has value <img src='https://latex.codecogs.com/svg.image?f(n-j)' title='f(n-j)' />. We choose the cut point that yields highest value. Thus

<img src='https://latex.codecogs.com/svg.image?\displaystyle&space;f(n)&space;=&space;\max_{1\leq&space;j&space;\leq&space;n}\{p_j&space;&plus;&space;f(n&space;-&space;j)\}' title='\displaystyle&space;f(n)&space;=&space;\max_{1\leq&space;j&space;\leq&space;n}\{p_j&space;&plus;&space;f(n&space;-&space;j)\}' />.

## Word Break

Now let 

<img src='https://latex.codecogs.com/svg.image?f:\{1,2,\ldots,&space;n\}\to\{T,&space;F\}' title='f:\{1,2,\ldots,&space;n\}\to\{T,&space;F\}' /> 

denote the value function for this word break problem, where <img src='https://latex.codecogs.com/svg.image?n' title='n' /> is the size of the string. We have to choose a break in the string, just like we have to choose a cut point in the rod-cutting problem. Any such break <img src='https://latex.codecogs.com/svg.image?j' title='j' /> would divide the string into two parts: a part that has Boolean value <img src='https://latex.codecogs.com/svg.image?\texttt{[s[j:n]&space;in&space;wordDict]}' title='\texttt{[s[j:n]&space;in&space;wordDict]}' />, and a part that has Boolean value <img src='https://latex.codecogs.com/svg.image?f(j)' title='f(j)' />. The value of such break is 

<img src='https://latex.codecogs.com/svg.image?\texttt{[s[j:n]&space;in&space;wordDict]}&space;\wedge&space;f(j)' title='\texttt{[s[j:n]&space;in&space;wordDict]}&space;\wedge&space;f(j)' />.  

Remamber that the function has only two values: True (<img src='https://latex.codecogs.com/svg.image?T' title='T' />) or False (<img src='https://latex.codecogs.com/svg.image?F' title='F' />). Any break that has True value is the optimal one. Thus the DP equation is

<img src='https://latex.codecogs.com/svg.image?\displaystyle&space;f(n)&space;=&space;\bigvee_{1\leq&space;j\leq&space;n}\left\{\texttt{[s[j:n]&space;in&space;wordDict]}&space;\wedge&space;f(j)\right\}' title='\displaystyle&space;f(n)&space;=&space;\bigvee_{1\leq&space;j\leq&space;n}\left\{\texttt{[s[j:n]&space;in&space;wordDict]}&space;\wedge&space;f(j)\right\}' />.

Looking at those two DP equations, we see that the _any_ operation "<img src='https://latex.codecogs.com/svg.image?\bigvee' title='\bigvee' />" in the bottom one corresponds to the <img src='https://latex.codecogs.com/svg.image?\max' title='\max' /> operation in the top one, and the _and_ operation "<img src='https://latex.codecogs.com/svg.image?\wedge' title='\wedge' />" corresponds to the plus operation "<img src='https://latex.codecogs.com/svg.image?&plus;' title='&plus;' />" in the top one.

Python code below.

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        f = [True]
        for i in range(1, len(s)+1):
            f += any(f[j] and s[j:i] in wordDict for j in range(i)),
        return f[-1]
```