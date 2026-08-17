class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixList = [1] * len(nums)
        suffixList = [1] * len(nums)

        prefix = 1
        suffix = 1

        for i in range(len(nums)):
            prefixList[i] = prefix  
            if i != 0: 
                prefix *= nums[i]
               

        for i in range(len(nums)-1, 0, -1): 
            suffixList[i] = suffix 
            if i != len(nums)-1: 
                suffix *= nums[i]

        res = []
        for i in range(len(suffixList)): 
            res.append(suffixList[i] * prefixList[i])

        return res