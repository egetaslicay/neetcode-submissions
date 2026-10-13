class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {} 

        def recurse(indexOfCoins: int, amountLeft: int) -> int: 
            if(amountLeft < 0): 
                return 0 

            if(amountLeft == 0): 
                return 1

            if (indexOfCoins, amountLeft) in memo: 
                return memo[(indexOfCoins, amountLeft)]

            count = 0 

            count += recurse(indexOfCoins, amountLeft - coins[indexOfCoins])
            
            if indexOfCoins < len(coins)-1: 
                count += recurse(indexOfCoins+1, amountLeft)

            memo[(indexOfCoins, amountLeft)] = count 
            return memo[(indexOfCoins, amountLeft)]

        return recurse(0, amount)