class Solution:
    def reverse(self, x: int) -> int:
        result = str(x)
        if result[0] == '-':
            neg = True
        else:
            neg = False
        result = result.replace('-', '')
        result = result[::-1]
        
        def rm0(s):
            i = 0
            while s[i] == 0:
                i = i + 1
            return s[i:]
        result = rm0(result)
        
        result = int(result)
        if result > 2**31 - 1:
            return 0
        if neg:
            return -result
        else:
            return result