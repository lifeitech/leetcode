# 206. Reverse Linked List

The recursive solution is given below.

```python
class Solution:
    def reverseList(self, x: ListNode) -> ListNode:
        if x == None or x.next == None:
            return x
        return_value = self.reverseList(x.next)
        x.next.next = x
        x.next = None 
        return return_value
```

Let's take the linked list $1\to2\to3\to4\to\varnothing$ as an example and walk through the code. I'll abbreviate `reverseList` as `f`. The initial input is `1`. What is `f(1)`? As the code indicates, it is `f(1.next) = f(2)`. The code can be rewritten as psudocode

```python
f(1):
    r = f(2)
    1.next.next = 1
    1.next = None
    return r
```

So it sets `2.next` to `1`, and sets `1.next` to `None`, which is desired. Now what is `f(2)`? It is

```python
f(2):
    r = f(3)
    2.next.next = 2
    2.next = None
    return r
```

So during the calculation of `f(2)`, `3.next` is set to `2`, but `2.next` is set to `None`. I was initially confused as to why `2.next` is set to `None`, cause in the final output `2.next` should be `1`, not `None`. The thing to note is that evaluation of `f(2)` is performed _before_ `2.next` is set to `1` in evaluation of `f(1)` (look at the body of `f(1)` above), so this will not cause incorrect assignments.  

Let's continue: the return value of `f(2)` is `f(3)`. What is `f(3)`? It is

```python
f(3):
    r = f(4)
    3.next.next = 3
    3.next = None
    return r
```

What is `f(4)`? Since `4.next == None`, `f(4) = 4` by the first two lines of the function `reverseList`. Thus we have gone through the process

* $\qquad\qquad\qquad\varnothing \leftarrow 3 \leftarrow 4$
* $\qquad\qquad\varnothing \leftarrow 2 \leftarrow 3$
* $\qquad\varnothing \leftarrow 1 \leftarrow 2$

And the return value for the input head `1` is `f(1) = f(2) = f(3) = f(4) = 4`, the new head for the reversed linked list.

This is the recursion: the code is written in a forward manner but the steps are performed backward. 