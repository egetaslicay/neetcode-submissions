class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix) 
        COLS = len(matrix[0])

        top = 0 
        bot = ROWS - 1

        while(top <= bot): 
            row = (top + bot) // 2
            if target > matrix[row][-1]: 
                top = row + 1 
            elif target < matrix[row][0]:
                bot = row - 1
            else: 
                break

        if not (top <= bot): 
            return False

        row = (top + bot)//2 
        left = 0 
        right = len(matrix)-1

        while(left <= right): 
            mid = left + (right-left)//2 

            if(matrix[row][mid] < target): 
                left = mid + 1
            elif(matrix[row][mid] > target): 
                right = mid - 1
            else: 
                return True


        return False