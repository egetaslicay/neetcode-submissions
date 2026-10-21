class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        numMinutes = -1

        for row in range(ROWS): 
            for col in range(COLS): 
                if grid[row][col] == 2: 
                    queue.append((row, col))

        while queue: 
            numToPop = len(queue)

            for i in range(numToPop): 
                row, col = queue.popleft() 
                
                # rot this one 
                grid[row][col] = 2 

                for r, c in directions: 
                    nrow = row + r
                    ncol = col + c 

                    if nrow >= 0 and nrow < ROWS and ncol >= 0 and ncol < COLS and grid[nrow][ncol] == 1: 
                        queue.append((nrow, ncol))

            numMinutes += 1 


        for row in range(ROWS): 
            if 1 in grid[row]: 
                return -1 

        return numMinutes






        

