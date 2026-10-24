class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set() 
        directions = [(1,0), (0,1), (-1,0), (0,-1)]



        def dfs(row, col) -> int: 
            if (row, col) in visited: 
                return 0 
            
            visited.add((row,col))

            res = 0 
            
            for dir in directions: 
                nrow = row + dir[0]
                ncol = col + dir[1] 

                if nrow >= ROWS or ncol >= COLS or ncol < 0 or nrow < 0: 
                    res += 1 
                elif grid[nrow][ncol] == 0: 
                    res += 1 
                else: 
                    res += dfs(nrow, ncol)

            return res 


        for row in range(ROWS): 
            for col in range(COLS): 
                if grid[row][col] == 1: 
                    return dfs(row, col)

        


            