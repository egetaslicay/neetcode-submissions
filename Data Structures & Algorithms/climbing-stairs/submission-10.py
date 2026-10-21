class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {} 
        memo[1] = 1
        memo[2] = 2

        def dp(stair: int): 
            if stair in memo: 
                return memo[stair]

            res = dp(stair-1) + dp(stair-2)
            memo[stair] = res 
            return memo[stair]

        return dp(n)

