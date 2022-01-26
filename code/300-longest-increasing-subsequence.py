class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
      n = len(nums)
      if n == 0:
        return 0
      f = [1] * n
      for i in range(1, n):
        v = 0
        for j in range(i):
          if nums[j] < nums[i]:
            v = max(v, f[j])
        f[i] = v + 1
      return max(f)