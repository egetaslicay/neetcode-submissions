class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visitedPacific = set() 
        visitedAtlantic = set() 

        ROWS = len(heights) 
        COLS = len(heights[0])

        res = [] 

        # dfs function 
        def dfs(row, col, visited):
            if (row, col) in visited: 
                return 

            visited.add((row,col))
            currVal = heights[row][col]

            if row > 0 and heights[row-1][col] >= currVal: 
                dfs(row-1, col, visited)

            if row < ROWS - 1 and heights[row+1][col] >= currVal:
                dfs(row+1, col, visited)

            if col > 0 and heights[row][col-1] >= currVal: 
                dfs(row, col-1, visited)

            if col < COLS-1 and heights[row][col+1] >= currVal: 
                dfs(row, col+1, visited)

    
        # loop through all top row: # pacific 
        for col in range(COLS): 
            dfs(0, col, visitedPacific)

        # loop through all first column: 
        for row in range(ROWS): 
            dfs(row, 0, visitedPacific)

        # loop through all bottom row:
        for col in range(COLS): 
            dfs(ROWS-1, col, visitedAtlantic)

        # loop through all last column: 
        for row in range(ROWS): 
            dfs(row, COLS-1, visitedAtlantic)

        # loop through both sets and find matching indexes 
        for entry in visitedPacific: 
            if entry in visitedAtlantic: 
                row, col = entry
                res.append([row,col])

        return res 
