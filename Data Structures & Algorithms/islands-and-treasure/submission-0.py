class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque() 
        ROWS = len(grid)
        COLS = len(grid[0]) 

        for row in range(ROWS): 
            for col in range(COLS):
                if grid[row][col] == 0: 
                    queue.append((row, col))


        while queue:
            current = queue 
            queue = deque() 

            for row, col in current: 
                
                # up 
                if row > 0 and grid[row-1][col] == 2**31-1: 
                    grid[row-1][col] = grid[row][col]+1 
                    queue.append((row-1, col))

                # down
                if row < ROWS - 1 and grid[row+1][col] == 2**31-1:
                    grid[row+1][col] = grid[row][col]+1 
                    queue.append((row+1, col))

                # left 
                if col > 0 and grid[row][col-1] == 2**31-1: 
                    grid[row][col-1] = grid[row][col]+1 
                    queue.append((row, col-1))

                # right 
                if col < ROWS - 1 and grid[row][col+1] == 2**31-1:
                    grid[row][col+1] = grid[row][col]+1 
                    queue.append((row, col+1))

                
                





        # no return statement 