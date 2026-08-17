class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixList = [1] * len(nums)
        suffixList = [1] * len(nums)

        prefix = 1
        suffix = 1

        for i in range(len(nums)): 
            prefixList[i] = prefix 
            prefix *= nums[i]
               

        for i in range(len(nums)-1, 0, -1): 
            suffixList[i] = suffix 
            suffix *= nums[i]

        res = []
        for i in range(len(suffixList)): 
            res.append(suffixList[i] * prefixList[i])

        return res