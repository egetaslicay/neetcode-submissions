class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {} 
        
        def dp(amountLeft: int) -> int: 
            if amountLeft in memo: 
                return memo[amountLeft]

            if amountLeft == 0: 
                return 0  

            res = float('inf')

            for j in range(len(coins)):
                if amountLeft - coins[j] >= 0: 
                    res = min(res, 1 + dp(amountLeft-coins[j]))

            memo[amountLeft] = res
            return memo[amountLeft]


        final = dp(amount) 

        if final == float('inf'): 
            return -1
        else: 
            return final