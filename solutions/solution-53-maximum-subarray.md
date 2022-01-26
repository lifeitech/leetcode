# 53. Maximum Subarray

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
         """
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)
        return max(nums)
```

What does this code mean? 

The last element of the maximum subarray _must_ lie in the input array. So for $i=1,\ldots,n$ we can define a function $f(i)$ that returns the output value if element $i$ _has to be_ the last element of the maximum subarray. Given that element $i$ must be included in the maximum subarray, what is the relationship between $f(i)$ and $f(i-1)$? If $f(i-1)$ is larger than $0$, then adding $f(i-1)$ to `nums[i]` certainly will improve `nums[i]`, no matter whether `nums[i]` is larger or smaller than $0$. If $f(i-1)$ is smaller than $0$, then adding $f(i-1)$ can only decrease `nums[i]`, so in this case $f(i)=$`nums[i]` and the maximum subarray that has to end in `nums[i]` consists of the element `nums[i]` alone. In summary,

$f(i) = \texttt{nums[i]} + \max\{f(i-1), 0\}$.

Again, the maximum subarray has to end somewhere in the input array, so after we computed the value for every element in the array, we can select the one with the maximum value. This element is the true last element of the maximum subarray. 

The code did not create a new array `f[i]` to store the values of the function, because it is convenient enough to modify the value on the original array, so we do not need to create this extra space. 
