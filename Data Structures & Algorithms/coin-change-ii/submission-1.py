class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}   

        def dp(index: int, amountLeft: int) -> int: 
            if (index, amountLeft) in memo: 
                return memo[(index, amountLeft)]

            if amountLeft == 0: 
                return 1 

            if index >= len(coins) or amountLeft < 0: 
                return 0 

            res = 0 

            res += dp(index, amountLeft - coins[index])     # take and stay at this number 
            res += dp(index + 1, amountLeft)                # dont take and move on 

            memo[(index, amountLeft)] = res 
            return memo[(index, amountLeft)]

        return dp(0, amount)


            
        
            