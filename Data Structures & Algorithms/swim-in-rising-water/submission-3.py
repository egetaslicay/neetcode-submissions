class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        heap = [] 
        ROWS = len(grid)
        COLS = len(grid[0])

        heapq.heappush(heap, (grid[0][0], 0, 0))
        directions = [(0,1), (1,0), (-1, 0), (0,-1)]

        while heap: 
            maxSF, row, col = heapq.heappop(heap)

            if (row == ROWS-1 and col == COLS-1): 
                return maxSF 

            if (row, col) in visited: 
                continue 
            
            visited.add((row, col))

            for dir in directions: 
                nrow = dir[0] + row 
                ncol = dir[1] + col

                if nrow < ROWS and nrow >= 0 and ncol < COLS and ncol >= 0 and (nrow, ncol) not in visited: 
                    heapq.heappush(heap, (max(maxSF, grid[nrow][ncol]), nrow, ncol))


        
            


                

            
            
             