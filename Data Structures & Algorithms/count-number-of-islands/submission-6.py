class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        count = 0 
        startingList = []
        directions = [(0,1), (1, 0), (-1, 0), (0, -1)]

        def dfs(row: int, col: int) -> None: 
                grid[row][col] = "0"

                for dir in directions:
                    nrow = row + dir[0]
                    ncol = col + dir[1]

                    if nrow >= 0 and nrow < ROWS and ncol >= 0 and ncol < COLS and grid[nrow][ncol] == "1": 
                        dfs(nrow, ncol)


        for row in range(ROWS): 
            for col in range(COLS): 
                if grid[row][col] == "1":
                    count += 1
                    dfs(row, col)


        return count 




        
        
            
