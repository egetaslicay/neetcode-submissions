class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        count = 0 

        def dfs(row, col, board: List[List[str]]): 
            if row < 0 or row >= ROWS or col < 0 or col >= COLS: 
                return 

            if board[row][col] == "0":
                return 


            board[row][col] = "0"
            dfs(row+1, col, board)
            dfs(row-1, col, board)
            dfs(row, col-1, board)
            dfs(row, col+1, board)


        for row in range(ROWS): 
            for col in range(COLS):

                if grid[row][col] == "1": 
                    count += 1
                    dfs(row, col, grid)


        return count 


