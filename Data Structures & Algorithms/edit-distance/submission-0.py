class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {} 

        def minOperations(i: int, j: int) -> int: 
            if (i, j) in memo: 
                return memo[(i, j)]

            if i == len(word1): 
                return len(word2)-j 

            if j == len(word2): 
                return len(word1)-i

            res = float('inf')

            if word1[i] == word2[j]:
                res = min(res, minOperations(i+1, j+1))
            else: 
                # replace i + 1 , j + 1 
                res = min(res, 1 + minOperations(i+1, j+1))
                # delete character
                res = min(res, 1 + minOperations(i+1, j)) 
                # insert a character 
                res = min(res, 1 + minOperations(i, j+1)) 

            memo[(i,j)] = res 
            return memo[(i, j)]

        return minOperations(0,0)
