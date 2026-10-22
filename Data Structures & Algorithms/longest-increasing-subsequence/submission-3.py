class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {} 

        def dp(i: int, previous: int) -> int: 
            if (i, previous) in memo: 
                return memo[(i, previous)]

            if i >= len(nums): 
                return 0 
        
            res = 0 

            if nums[i] > previous: 
                res = max(res, 1 + dp(i + 1, nums[i]))
            
            res = max(res, dp(i + 1, previous))

            memo[(i, previous)] = res 
            return memo[(i, previous)]

        return dp(0, float('-inf'))
