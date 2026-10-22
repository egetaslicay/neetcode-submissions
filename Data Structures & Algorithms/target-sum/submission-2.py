class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {} 

        
        def dp(index: int, sumSF: int) -> int: 
            if (index, sumSF) in memo: 
                return memo[(index, sumSF)]

            if (sumSF == target and index == len(nums)): 
                return 1

            if index >= len(nums): 
                return 0 

            res = 0 

            res += dp(index + 1, sumSF + nums[index])
            res += dp(index + 1, sumSF - nums[index])

            memo[(index, sumSF)] = res 
            return memo[(index, sumSF)]

        return dp(0, 0)