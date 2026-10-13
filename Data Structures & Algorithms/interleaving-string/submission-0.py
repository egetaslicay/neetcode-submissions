class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}

        if len(s1) + len(s2) != len(s3): 
            return False

        def recurse(i: int, j: int) -> bool: 
            if (i, j) in memo: 
                return memo[(i,j)]

            if i + j == len(s3): 
                return True

            result = False

            if(i < len(s1) and s3[i+j] == s1[i]): 
                result = result or recurse(i+1, j)

            if(j < len(s2) and s3[i+j] == s2[j]):
                result = result or recurse(i, j+1)

            

            memo[(i, j)] = result
            return memo[(i, j)]


        return recurse(0,0)