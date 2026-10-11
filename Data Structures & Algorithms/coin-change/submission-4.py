class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {} 
        # want to return the minimum number of coins 
        def minCoins(whatsLeft: int) -> int: 
            count = float('inf')
            
            if whatsLeft in memo: 
                return memo[whatsLeft]

            if whatsLeft == 0: 
                return 0

            if whatsLeft < 0: 
                return float('inf')

            for i in range(len(coins)):
                count = min(1 + minCoins(whatsLeft - coins[i]), count)

            memo[whatsLeft] = count 
            return memo[whatsLeft]

        
        call = minCoins(amount)

        if call == float('inf'): 
            return -1

        return call 