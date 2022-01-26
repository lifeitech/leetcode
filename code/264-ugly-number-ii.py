class Solution:
    def nthUglyNumber(self, n: int) -> int:
        f = [1]
        p2 = p3 = p5 = 0
        for i in range(n-1):
            next_number = min(f[p2]*2, f[p3]*3, f[p5]*5)
            f.append(next_number)
            if f[-1] == f[p2]*2:
                p2 += 1
            if f[-1] == f[p3]*3:
                p3 += 1
            if f[-1] == f[p5]*5:
                p5 += 1
        return f[-1]