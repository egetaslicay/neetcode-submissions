class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        directions = [(1,0), (0,1)]
        memo = {} 

        def dp(row, col) -> int: 
            if (row, col) in memo: 
                return memo[(row, col)]

            if (row == ROWS - 1 and col == COLS - 1): 
                return 1 

            res = 0 

            for r, c in directions: 
                nrow = r + row 
                ncol = c + col 

                if ncol < COLS and nrow < ROWS and ncol >= 0 and nrow >= 0 and obstacleGrid[nrow][ncol] != 1: 
                    res += dp(nrow, ncol)

            memo[(row, col)] = res 
            return res 

        return dp(0, 0)



            