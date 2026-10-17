class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        furthestIndex = 0 

        for i in range(len(nums)): 
            if i > furthestIndex: 
                return False 

            furthestIndex = max(furthestIndex, i + nums[i])

        return True 
            