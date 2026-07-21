class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix[0])-1 
        row = 0

        while(col >= 0 and row <= len(matrix)-1): 
            numAtPoint = matrix[row][col] 

            if(numAtPoint < target):
                row += 1
            else: 
                while(col >= 0): 
                    numAtPoint = matrix[row][col] 
                    if(numAtPoint == target): 
                        return True
                    else: 
                        col -= 1 

        return False
