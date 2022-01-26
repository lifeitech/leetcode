class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        if n==1:
            return 10
        result = 10
        g = 9
        i = 2
        while i<=n and i<=10:
            g = g * (10-i+1)
            result = result + g
            i = i + 1
        return result