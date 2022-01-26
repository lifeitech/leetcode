class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def f(arr):
            n = len(arr)
            r = [1]
            for i in range(1, n):
                r.append(arr[i-1] + arr[i]) 
            r.append(1)
            return r
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        triangle = [[1]]
        for j in range(numRows-1):
            triangle.append(f(triangle[-1]))
            
        return triangle