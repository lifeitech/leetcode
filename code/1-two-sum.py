class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, a in enumerate(nums):
            if target - a in table:
                return [i, table.get(target - a)]
            table[a] = i