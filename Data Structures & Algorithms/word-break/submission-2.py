class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {} 

        def canReconstruct(i: int) -> bool: 
            if i == len(s): 
                return True

            if i in memo: 
                return memo[i]

            result = False 

            for word in wordDict: 
                if s[i:i+len(word)].startswith(word): 
                    result = result or canReconstruct(i + len(word)) 

            
            memo[i] = result 
            return memo[i]


        return canReconstruct(0)


        