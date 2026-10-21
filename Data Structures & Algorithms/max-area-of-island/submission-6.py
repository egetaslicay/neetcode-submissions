class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0 
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0,1), (1,0), (-1, 0), (0, -1)]



        def dfs(row, col) -> int:
            if row < 0 or row >= ROWS or col < 0 or col >= COLS: 
                return 0 
            if grid[row][col] == 0: 
                return 0 

            grid[row][col] = 0
    
            area = 1 
            area += dfs(row + 1, col)
            area += dfs(row - 1, col)
            area += dfs(row, col + 1)
            area += dfs(row, col - 1)
            return area  


        for row in range(ROWS): 
            for col in range(COLS): 
                if grid[row][col] == 1: 
                    maxArea = max(maxArea, dfs(row, col))




        return maxArea 
