class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        lst = []
        for n in range(left, right+1):
            s = str(n)
            if '0' not in s:
                if all(n % i == 0 for i in set(int(i) for i in s)):
                    lst.append(n)
        return lst