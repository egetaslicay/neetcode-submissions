class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0 
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0,1), (1,0), (-1, 0), (0, -1)]



        def dfs(row, col) -> int:
            if grid[row][col] == 0: 
                return 0 

            grid[row][col] = 0
            res = 1
        
            for dir in directions:
                nrow = row + dir[0]
                ncol = col + dir[1]

                if nrow >= 0 and nrow < ROWS and ncol >= 0 and ncol < COLS and grid[nrow][ncol] == 1: 
                    res += dfs(nrow, ncol)

            return res 


        for row in range(ROWS): 
            for col in range(COLS): 
                if grid[row][col] == 1: 
                    maxArea = max(maxArea, dfs(row, col))




        return maxArea 
