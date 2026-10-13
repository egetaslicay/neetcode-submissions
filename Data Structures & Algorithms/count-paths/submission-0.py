class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {} 

        def dfs(row: int, col: int) -> int: 
            if (row, col) in memo: 
                return memo[row,col]
                 
            if row == m-1 and col == n-1: 
                return 1 

            count = 0 

            if row < m-1: 
                count += dfs(row+1, col)

            if col < n-1: 
                count += dfs(row, col+1)

            memo[(row,col)] = count 
            return memo[(row, col)]

        return dfs(0, 0)

        