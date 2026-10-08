class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0 
        ROWS = len(grid)
        COLS = len(grid[0])


        def dfs(row, col, board): 
            if row < 0 or row >= ROWS or col < 0 or col >= COLS: 
                return 0 

            if board[row][col] == 1: 
                board[row][col] = 0 
                return 1 + dfs(row+1, col, board) + dfs(row-1, col, board) + dfs(row, col+1, board) + dfs(row, col-1, board)
        
            else: 
                return 0

        for row in range(ROWS): 
            for col in range(COLS): 
                
                if grid[row][col] == 1:
                    maxArea = max(maxArea, dfs(row,col, grid))

        return maxArea 
