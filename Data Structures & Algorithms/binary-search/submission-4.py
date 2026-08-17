class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) -1 

        while(left <= right): 
            mid = left + (right - left)/2 

            if(nums[mid] < target): 
                left = mid + 1 
                continue
            elif(nums[mid] > target): 
                right = mid -1 
                continue
            else: 
                return mid
        
        return -1

            