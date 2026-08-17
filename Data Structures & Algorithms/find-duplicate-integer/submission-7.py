class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums: 
            index = abs(num)-1 
            if nums[index] > 0: 
                nums[index] *= -1
            else: 
                return num
        
        return -1 # not possible