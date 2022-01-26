class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        def isPrime(n):
            if n == 1:
                return False
            if n == 2:
                return True
            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i = i + 1
            return True
            
        
        lst = []
        for number in range(L, R+1):
            binary = bin(number)[2:]
            set_count = binary.count('1')
            if isPrime(set_count):
                lst.append(number)
        return len(lst)