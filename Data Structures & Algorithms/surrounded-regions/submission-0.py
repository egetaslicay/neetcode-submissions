class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board) 
        COLS = len(board[0])

        visited = set() 

        def dfs(row, col): 
            if (row, col) in visited: 
                return 

            visited.add((row,col))

            if row > 0 and board[row-1][col] == "O": 
                dfs(row-1, col)

            if row < ROWS - 1 and board[row+1][col]  == "O": 
                dfs(row+1, col)

            if col > 0 and board[row][col-1] == "O": 
                dfs(row, col-1)

            if col < COLS-1 and board[row][col+1] == "O": 
                dfs(row, col+1)
                
        
        for col in range(COLS):
            if board[0][col] == "O": 
                dfs(0, col)

        for col in range(COLS): 
            if board[ROWS-1][col] == "O": 
                dfs(ROWS-1, col)

        for row in range(ROWS): 
            if board[row][0] == "O": 
                dfs(row, 0)

        for row in range(ROWS): 
            if board[row][COLS-1] == "O": 
                dfs(row, COLS-1)

        for row in range(ROWS): 
            for col in range(COLS): 

                if board[row][col] == "O" and not (row,col) in visited: 
                    board[row][col] = "X"
    