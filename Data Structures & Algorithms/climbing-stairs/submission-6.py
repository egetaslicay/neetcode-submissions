class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[1] = 1 
        memo[2] = 2 

        def ways(k): 
            if k in memo: 
                return memo[k]

            memo[k] = ways(k-1) + ways(k-2)
            
            return memo[k]

        return ways(n)