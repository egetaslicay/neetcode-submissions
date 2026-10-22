class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {} 
        directions = [(1,0), (0,1), (0,-1), (-1, 0)]
        ROWS = len(matrix)
        COLS = len(matrix[0])

        def dfs(row, col) -> int: 
            if (row, col) in memo: 
                return memo[(row, col)]

            res = 1

            for dir in directions: 
                nrow = row + dir[0]
                ncol = col + dir[1]

                if nrow < ROWS and nrow >= 0 and ncol < COLS and ncol >= 0 and matrix[nrow][ncol] > matrix[row][col]: 
                    res = max(res, 1 + dfs(nrow, ncol))

            memo[(row, col)] = res
            return memo[(row, col)]

        result = 0

        for row in range(ROWS): 
            for col in range(COLS): 
                result = max(result, dfs(row, col))
        
        return result