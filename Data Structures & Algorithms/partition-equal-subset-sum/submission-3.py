class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        memo = {} 

        def dp(index: int, currSum: int) -> bool: 
            if (index, currSum) in memo: 
                return memo[(index, currSum)]

            if (total - currSum == currSum):
                return True 

            if(index >= len(nums)): 
                return False 

            res = False 

            if currSum + nums[index] <=  (total // 2): 
                res = res or dp(index + 1, currSum + nums[index])

            res = res or dp(index + 1, currSum)

            memo[(index, currSum)] = res 
            return memo[(index, currSum)] 

        return dp(0, 0)
