class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROWS = len(board)
        COLS = len(board[0])

        if not word: 
            return True

        def backtrack(row, col, i):  

            if i == len(word): 
                return True 

            if i >= len(word): 
                return False 

            result = False

            for dr in directions: 
                nrow = row + dr[0]
                ncol = col + dr[1]

                if (nrow, ncol) not in visited and nrow <= ROWS-1 and nrow >= 0 and ncol <= COLS-1 and ncol >= 0 and board[nrow][ncol] == word[i]: 
                    visited.add((nrow, ncol))
                    result = result or backtrack(nrow, ncol, i+1)
                    if result: 
                        return True 
                    visited.remove((nrow, ncol))

            return result 

        for row in range(ROWS):
            for col in range(COLS): 
                if board[row][col] == word[0]: 
                    visited.add((row,col))
                    if backtrack(row, col, 1): 
                        return True 
                    visited.remove((row,col))

        return False
                    
        

            


            