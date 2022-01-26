class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if sum(nums) < S or (sum(nums) + S) % 2 == 1: return 0
        target = (sum(nums) + S) // 2
        f = [1] + [0 for _ in range(target)]
        for i in range(len(nums)):
            for j in range(target,nums[i] - 1, -1):
                f[j]  = f[j] +  f[j - nums[i]]
        return f[target]