class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        S= [0]
        for x in A:
            S.append(S[-1] + x)
        def average(i, j):
            return (S[j] - S[i]) / float(j - i)
        
        N = len(A)
        f = [average(i, N) for i in range(N)]
        for k in range(K-1):
            for i in range(N):
                for j in range(i+1, N):
                    f[i] = max(f[i], average(i, j) + f[j])
        return f[0]