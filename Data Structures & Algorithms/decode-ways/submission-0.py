class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {} 

        def numWays(string: str) -> int:  
            if string in memo: 
                return memo[string]
                
            if not string: 
                return 1 

            # string is invalid 
            if string.startswith("0"): 
                return 0 

            count = 0
            count += numWays(string[1:])
            
            if len(string) >= 2 and int(string[:2]) <= 26: 
                count += numWays(string[2:])
            
            memo[string] = count
            return count 

        return numWays(s) 