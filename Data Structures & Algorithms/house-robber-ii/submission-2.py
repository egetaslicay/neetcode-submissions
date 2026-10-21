class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]


        def robline(array): 
            memo = {} 

            def dp(i): 
                if i in memo: 
                    return memo[i]

                if i >= len(array): 
                    return 0 

                res = 0 
                res = max(array[i] + dp(i+2), dp(i + 1))
                memo[i] = res
                return memo[i]
            
            return dp(0)

        return max(robline(nums[1:]), robline(nums[:-1]))
                




