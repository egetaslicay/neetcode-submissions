class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)): 
            index = nums[i]
            if(nums[index] > 0): 
                nums[index] *= -1 
            else: 
                return abs(nums[index])