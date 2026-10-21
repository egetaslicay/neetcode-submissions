class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        distance = 0 
        directions = [(0,1), (1,0), (-1,0), (0,-1)]


        for row in range(ROWS): 
            for col in range(COLS):
                if grid[row][col] == 0: 
                    queue.append((row, col)) 

        while queue: 
            numPops = len(queue)

            for i in range(numPops): 
                row, col = queue.popleft() 
                grid[row][col] = distance 

                for r,c in directions: 
                    nrow = row + r
                    ncol = col + c

                    if nrow >= 0 and nrow < ROWS and ncol >= 0 and ncol < COLS and grid[nrow][ncol] == 2147483647:
                        queue.append((nrow, ncol))
                        grid[nrow][ncol] = distance + 1 

                   
            distance += 1

                
        # no return statement 