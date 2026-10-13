class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {} 

        ROWS = len(matrix)
        COLS = len(matrix[0])

        def dfs(row: int, col: int) -> int: 
            if (row, col) in memo: 
                return memo[(row, col)]

            longest = 1 

            if row < ROWS-1 and matrix[row+1][col] > matrix[row][col]: 
                longest = max(longest, 1 + dfs(row+1, col))

            if row > 0 and matrix[row-1][col] > matrix[row][col]:
                longest = max(longest, 1 + dfs(row-1, col))

            if col < COLS-1 and matrix[row][col+1] > matrix[row][col]:
                longest = max(longest, 1 + dfs(row, col+1))
            
            if col > 0 and matrix[row][col-1] > matrix[row][col]:
                longest = max(longest, 1 + dfs(row, col-1))

            memo[(row, col)] = longest
            return memo[(row, col)]


        longest = 0 

        for row in range(ROWS): 
            for col in range(COLS): 
                longest = max(longest, dfs(row, col))

        return longest 