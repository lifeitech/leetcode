import numpy as np

class NumMatrix:

    def __init__(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        matrix = np.array(matrix)
        self.f = np.zeros(shape=matrix.shape, dtype=int)
        self.f[0,0] = matrix[0, 0]
        for i in range(1, self.f.shape[0]):
            self.f[i, 0] = self.f[i-1, 0] + matrix[i, 0]
            
        for j in range(1, self.f.shape[1]):
            self.f[0, j] = self.f[0, j-1] + matrix[0, j]
            
        for i in range(1, self.f.shape[0]):
            for j  in range(1, self.f.shape[1]):
                self.f[i, j] = self.f[i, j - 1] + self.f[i - 1, j] - self.f[i - 1, j - 1] + matrix[i, j]
        # print(self.f)


    def query(self, a, b):
        if a  < 0 or b < 0:
            return 0
        else:
            return self.f[a, b]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return self.query(row2, col2) - self.query(row2, col1 - 1) - self.query(row1 - 1, col2)  + self.query(row1 - 1, col1 - 1)