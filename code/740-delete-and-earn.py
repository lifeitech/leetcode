class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        f = [nums[0], max(nums[0],nums[1])]
        for k in range(2, n):
            f.append(max(f[k-2]+nums[k], f[k-1]))
        return f[-1]


    def deleteAndEarn(self, nums: List[int]) -> int:
        points = [0] * 10001
        for num in nums:
            points[num] += num
        return self.rob(points)