class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1,0), (0,1)]
        memo = {}  

        def dp(row, col): 
            if (row, col) in memo: 
                return memo[(row, col)]

            if row == ROWS - 1 and col == COLS - 1: 
                return grid[row][col]

            res = float('inf')

            for r, c in directions: 
                nrow = r + row 
                ncol = c + col 

                if ncol < COLS and nrow < ROWS and ncol >= 0 and nrow >= 0: 
                    res = min(res, grid[row][col] + dp(nrow, ncol))
            
            memo[(row,col)] = res 
            return res

        return dp(0,0)