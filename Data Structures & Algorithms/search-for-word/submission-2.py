class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set() 
        ROWS = len(board)
        COLS = len(board[0])
        directions = [(1,0), (0,1), (-1, 0), (0, -1)]

        def dfs(row, col, index) -> bool: 
            if (row, col) in visited: 
                return False 


            if index == len(word):
                return True 
            
            res = False 


            visited.add((row, col))

            for dir in directions: 
                nrow = row + dir[0]
                ncol = col + dir[1]

                if nrow < ROWS and ncol < COLS and ncol >= 0 and nrow >= 0 and board[nrow][ncol] == word[index]: 
                    call = dfs(nrow, ncol, index+1)

                    if call: 
                        return True 

            visited.remove((row, col))
            return res 


        for row in range(ROWS): 
            for col in range(COLS): 
                if board[row][col] == word[0]: 
                    call = dfs(row, col, 1)
                    if call: 
                        return True

        return False 

        
        