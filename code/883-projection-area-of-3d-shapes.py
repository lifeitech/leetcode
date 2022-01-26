class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        N = len(grid)
        r = 0
        for i in range(N):
            best_row = 0  # max of grid[i][j]
            best_col = 0  # max of grid[j][i]
            for j in range(N):
                if grid[i][j]:
                    r += 1  # top shadow
                best_row = max(best_row, grid[i][j])
                best_col = max(best_col, grid[j][i])

            r += best_row + best_col

        return r