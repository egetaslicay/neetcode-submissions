class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {} 

        def dp(i): 
            if i in memo: 
                return memo[i]

            if i >= len(cost): 
                return 0

            res = min(cost[i] + dp(i+1), cost[i] + dp(i+2))
            memo[i] = res
            return memo[i]



        return min(dp(0), dp(1))
        