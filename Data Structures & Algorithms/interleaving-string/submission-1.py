class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {} 

        if len(s1) + len(s2) != len(s3): 
            return False

        def dp(i: int, j: int) -> bool: 
            if (i, j) in memo: 
                return memo[(i,j)]

            if i == len(s1) and j == len(s2): 
                return True 

            res = False 

            if i < len(s1) and s3[i+j] == s1[i]: 
                res = res or dp(i+1, j)
            
            if j < len(s2) and s3[i+j] == s2[j]: 
                res = res or dp(i, j+1)

            memo[(i, j)] = res 
            return memo[(i, j)]

        return dp(0, 0)


            