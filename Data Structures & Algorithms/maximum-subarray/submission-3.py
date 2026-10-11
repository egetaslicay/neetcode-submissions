class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float('-inf')
        currSum = 0 

        for num in nums: 
            currSum += num 
            best = max(currSum, best)

            if currSum < 0: 
                currSum = 0 

        return best 