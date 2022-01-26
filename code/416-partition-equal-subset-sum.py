class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1: return 0
        target = s // 2
        f = [True] + [False for _ in range(target)]
        for i in range(len(nums)):
            for j in range(target,nums[i] - 1, -1):
                f[j]  = f[j] or  f[j - nums[i]]
        return f[target]