class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visitedPacific = set() 
        visitedAtlantic = set() 
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        ROWS = len(heights) 
        COLS = len(heights[0])

        res = [] 


        def pacificDFS(row, col): 
            if (row, col) in visitedPacific: 
                return 

            visitedPacific.add((row, col))

            for r, c in directions: 
                nrow = row + r
                ncol = col + c 

                if nrow >= 0 and nrow < ROWS and ncol >= 0 and ncol < COLS and heights[nrow][ncol] >= heights[row][col]:
                    pacificDFS(nrow, ncol) 
        
        def atlanticDFS(row, col): 
            if (row, col) in visitedAtlantic: 
                return 

            visitedAtlantic.add((row, col))

            for r, c in directions: 
                nrow = row + r
                ncol = col + c 

                if nrow >= 0 and nrow < ROWS and ncol >= 0 and ncol < COLS and heights[nrow][ncol] >= heights[row][col]:
                    atlanticDFS(nrow, ncol) 
            
        for row in range(ROWS): 
            pacificDFS(row, 0)
        
        for col in range(COLS):
            pacificDFS(0, col)

        for row in range(ROWS): 
            atlanticDFS(row, COLS-1)
        
        for col in range(COLS):
            atlanticDFS(ROWS-1, col)

        for entry in visitedPacific: 
            if entry in visitedAtlantic: 
                res.append(entry) 

        return res 
