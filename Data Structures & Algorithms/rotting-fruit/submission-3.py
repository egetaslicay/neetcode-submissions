class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque() 
        numMinutes = 0 


        # add all the 
        for row in range(ROWS): 
            for col in range(COLS): 
                if grid[row][col] == 2: 
                    queue.append((row, col))


        while queue: 
            current = queue
            queue = deque() 
            
            for row, col in current:

                # up 
                if row > 0 and grid[row-1][col] == 1: 
                    grid[row-1][col] = 2
                    queue.append((row-1, col))

                # down
                if row < ROWS-1 and grid[row+1][col] == 1: 
                    grid[row+1][col] = 2
                    queue.append((row+1, col))

                # left
                if col > 0 and grid[row][col-1] == 1: 
                    grid[row][col-1] = 2
                    queue.append((row, col-1))

                # right 
                if col < COLS-1 and grid[row][col+1] == 1:
                    grid[row][col+1] = 2
                    queue.append((row, col+1))

            if queue: 
                numMinutes += 1

        for row in range(ROWS): 
            if 1 in grid[row]: 
                return -1 

        return numMinutes 






        

