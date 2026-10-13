class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def lcs(i: int, j: int) -> int: 
            if (i,j) in memo: 
                return memo[(i,j)] 

            if i >= len(text1) or j >= len(text2): 
                return 0 

            longest = 0 

            if text1[i] == text2[j]: 
                longest = 1+lcs(i+1, j+1)
            else: 
                longest = max(longest, lcs(i+1, j))
                longest = max(longest, lcs(i, j+1))

            memo[(i,j)] = longest 
            return memo[(i,j)]

        return lcs(0, 0)