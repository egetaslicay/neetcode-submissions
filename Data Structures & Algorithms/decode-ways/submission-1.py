class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {} 

        def dp(i: int) -> int: 
            if i in memo: 
                return memo[i]

            if i >= len(s): 
                return 1 
            
            res = 0 
            if not s[i:i+1].startswith("0"): 
                res += dp(i+1)

            if not s[i:i+2].startswith("0") and int(s[i:i+2]) >= 10 and int(s[i:i+2]) <= 26: 
                res += dp(i+2)
            
            memo[i] = res
            return memo[i]


        return dp(0) 