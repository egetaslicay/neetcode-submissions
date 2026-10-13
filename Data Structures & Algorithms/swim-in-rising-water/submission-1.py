class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [] 
        heapq.heappush(heap, (grid[0][0], 0, 0))
        COLS = len(grid[0])
        ROWS = len(grid)
        visited = set() 

        while heap:
            maxPath, row, col = heapq.heappop(heap)
            if (row, col) not in visited: 
                visited.add((row, col))
                # base case check 
                if row == ROWS-1 and col == COLS-1:
                    return maxPath  

                # up 
                if row > 0 and (row-1, col) not in visited: 
                    heapq.heappush(heap, (max(maxPath, grid[row-1][col]), row-1, col))

                # down 
                if row < ROWS-1 and (row+1, col) not in visited: 
                    heapq.heappush(heap,(max(maxPath, grid[row+1][col]), row+1, col))
            
                # left 
                if col > 0 and (row, col-1) not in visited: 
                    heapq.heappush(heap, (max(maxPath, grid[row][col-1]), row, col-1))

                # right 
                if col < COLS -1 and (row, col+1) not in visited: 
                    heapq.heappush(heap, (max(maxPath, grid[row][col+1]), row, col+1))

            
             