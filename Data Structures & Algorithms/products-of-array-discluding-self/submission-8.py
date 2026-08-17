class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixList = [1] * len(nums)
        suffixList = [1] * len(nums)

        prefix = 1
        suffix = 1

        for i in range(len(nums)): 
            if i != 0: 
                prefix *= nums[i]
                prefixList[i] = prefix 

        for i in range(len(nums)-1, 0, -1): 
            if i != len(nums)-1: 
                suffix *= nums[i]
                suffixList[i] = suffix 

        res = []
        for i in range(len(suffixList)): 
            res.append[suffixList[i] * prefixList[i]]

        return res