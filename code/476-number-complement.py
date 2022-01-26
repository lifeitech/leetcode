class Solution:
    def findComplement(self, num: int) -> int:
        x = '1' * (len(bin(num)) - 2)
        return int(x, 2) ^ num