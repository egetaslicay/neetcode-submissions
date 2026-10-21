class Solution:
    def rob(self, nums: List[int]) -> int: 
        memo = {} 

        def dp(i: int) -> int: 
            if i in memo: 
                return memo[i]

            if i >= len(nums): 
                return 0 

            res = 0 
            res = max(nums[i] + dp(i + 2), 0 + dp(i + 1)) 
            memo[i] = res
            return memo[i]

        return dp(0)

