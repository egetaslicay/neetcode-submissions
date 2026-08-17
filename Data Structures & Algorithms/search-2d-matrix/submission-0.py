class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0 

        while(row <= len(matrix)):
            left = 0 
            right = len(matrix[0])
            nums = matrix[row]

            if(target >= nums[left] and target <= nums[right]): 
                while(left <= right): 
                    mid = left + (right - left)//2 

                    if(nums[mid] == target): 
                        return True
                    elif(nums[mid] > target): 
                        left = mid + 1
                    elif(nums[mid] < target): 
                        right = mid - 1
                    else: 
                        return False
            else: 
                row += 1


        return False