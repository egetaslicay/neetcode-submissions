class Solution:
    def solve(self, board: List[List[str]]) -> None:    
        ROWS = len(board)
        COLS = len(board[0])
        directions = [(1,0), (0, 1), (-1, 0), (0, -1)]
        
        def dfs(row: int, col: int): 
            if board[row][col] != "O": 
                return 

            board[row][col] = "G"

            for r,c in directions:
                nrow = r + row 
                ncol = c + col 

                if nrow >= 0 and nrow < ROWS and ncol >= 0 and ncol < COLS and board[nrow][ncol] == "O": 
                    dfs(nrow,ncol) 

        for row in range(ROWS): 
            for col in range(COLS): 
                if row == 0 or row == ROWS-1 or col == 0 or col == COLS -1: 
                    dfs(row, col)


        for row in range(ROWS): 
            for col in range(COLS): 
                if board[row][col] == "G": 
                    board[row][col] = "O"
                else: 
                    board[row][col] = "X"
        
