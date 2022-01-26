import numpy as np
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        board = np.array(board)
        x, y = np.where(board == 'R')
        count = 0
        
        i = x
        while i >= 0 and board[i, y] != 'B':
            if board[i, y] == 'p':
                count = count + 1
                break
            i = i - 1
        
        i = x
        while i <= 7 and board[i, y] != 'B':
            if board[i, y] == 'p':
                count = count + 1
                break
            i = i + 1
            
        j = y
        while j >= 0 and board[x, j] != 'B':
            if board[x, j] == 'p':
                count = count + 1
                break
            j = j - 1
        
        j = y
        while j <= 7 and board[x, j] != 'B':
            if board[x, j] == 'p':
                count = count + 1
                break
            j = j + 1
            
        return count