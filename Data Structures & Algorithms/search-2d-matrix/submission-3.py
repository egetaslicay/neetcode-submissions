class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0 

        while(row <= len(matrix)-1):
            left = 0 
            right = len(matrix[0])-1
            nums = matrix[row]

            if(target >= nums[left] and target <= nums[right]): 
                while(left <= right): 
                    mid = left + (right - left)//2 

                    if(nums[mid] < target): 
                        left = mid + 1 
                        continue
                    elif(nums[mid] > target): 
                        right = mid -1 
                        continue
                    else: 
                        return True
        
            row += 1


        return False