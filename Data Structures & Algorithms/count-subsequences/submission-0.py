class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {} 

        
        def dp(i: int, j: int) -> int: 
            if (i, j) in memo: 
                return memo[(i, j)]

            if j == len(t): 
                return 1 

            if i >= len(s): 
                return 0 

            res = 0 

            # if they are equivalent take from s and increase t 
            if s[i] == t[j]: 
                res += dp(i+1, j+1)
    
            res += dp(i+1, j)

            memo[(i, j)] = res 
            return memo[(i, j)]

        return dp(0, 0)

            
            

            