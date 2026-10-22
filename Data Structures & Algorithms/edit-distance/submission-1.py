class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {} 

        def dp(i: int, j: int) -> int: 
            if (i, j) in memo: 
                return memo[(i,j)]

            if i == len(word1) and j == len(word2): 
                return 0 

            if i == len(word1): 
                return len(word2) - j 

            if j == len(word2): 
                return len(word1) - i 

            numOperations = float('inf')
            
            if i < len(word1) and j < len(word2) and word1[i] == word2[j]:
                numOperations = min(numOperations, dp(i + 1, j + 1))
            
            # insert
            numOperations = min(numOperations, dp(i, j + 1) + 1)

            # delete
            numOperations = min(numOperations, dp(i + 1, j) + 1)

            # replace a character 
            numOperations = min(numOperations, dp(i + 1, j + 1) + 1)

            memo[(i, j)] = numOperations
            return numOperations 
        
        return dp(0, 0)

