class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0 
        right = len(matrix)-1 

        while(left <= right): 
            mid = (left+right)//2

            if(matrix[mid][0] <= target): 
                # we found a good one 
                if(target <= matrix[mid][-1]): 
                    break 
                else: 
                    left = mid + 1
            else: 
                right = mid-1

        if right < left: 
            return False 


        searchRow = matrix[mid]
        lo = 0 
        hi = len(searchRow)-1
        

        while lo <= hi: 
            mid = (hi+lo)//2

            if(searchRow[mid] < target): 
                lo = mid + 1
            elif(searchRow[mid] > target): 
                hi = mid - 1 
            else: 
                return True 

        return False
