class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        currSum = nums[0]

        for i in range(1, len(nums)):
            if currSum < 0: 
                currSum = nums[i]
            else:
                currSum = currSum + nums[i]
                res = max(res, currSum)

        return res 

