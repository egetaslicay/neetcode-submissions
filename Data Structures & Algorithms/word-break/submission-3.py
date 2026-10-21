class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {} 

        def dp(index: int) -> bool: 
            if index in memo: 
                return memo[index]

            if index == len(s): 
                return True 

            result = False 

            for j in range(len(wordDict)): 
                if s[index:].startswith(wordDict[j]) and index + len(wordDict[j]) <= len(s):
                    result = result or dp(index + len(wordDict[j]))

            memo[index] = result 
            return  memo[index]

        return dp(0)


        