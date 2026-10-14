class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        counter = 1
        queue = deque() 
        visited = set() 
        ROWS = len(grid)
        COLS = len(grid[0])
        direction = [(1,0), (0,1), (-1,0), (0,-1), (-1,-1), (1,-1), (-1, 1), (1,1)]

        if grid[0][0] == 1: 
            return -1 

        queue.append((0,0))


        while queue:
            numToPop = len(queue) # length of one level 

            for i in range(numToPop):  # pop one level # of times 
                row, col = queue.popleft() 
                visited.add((row,col))

                if row == ROWS-1 and col == COLS-1: 
                    return counter

                for dir in direction: 
                    newRow = row + dir[0]
                    newCol = col + dir[1]

                    if newRow <= ROWS-1 and newCol <= COLS-1 and newRow >= 0 and newCol >= 0 and grid[newRow][newCol] != 1 and (newRow, newCol) not in visited: 
                        queue.append((newRow, newCol))

            counter += 1  # after one level is popped increase the number of steps 

        return -1 

