class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {} 
        ROWS = m 
        COLS = n
        directions = [(1, 0), (0, 1)]

        def dp(row: int, col: int) -> int: 
            if (row, col) in memo: 
                return memo[(row,col)]

            if row == ROWS-1 and col == COLS-1: 
                return 1 

            res = 0 

            for dir in directions: 
                nrow = row + dir[0]
                ncol = col + dir[1]
                 
                if nrow < ROWS and nrow >= 0 and ncol < COLS and ncol >= 0: 
                   res += dp(nrow, ncol)

            memo[(row, col)] = res 
            return memo[(row, col)]

        return dp(0, 0)


        