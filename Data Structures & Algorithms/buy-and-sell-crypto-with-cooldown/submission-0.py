class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {} 


        def dp(day: int, holding: bool): 
            if (day, holding) in memo: 
                return memo[(day, holding)]

            if day >= len(prices): 
                return 0 
            
            res = 0 


            if holding: 
                res = max(res, dp(day+2, False) + prices[day]) # try selling 
                res = max(res, dp(day+1, True))
            else: 
                res = max(res, dp(day+1, True)  - prices[day])# buy this one 
                res = max(res, dp(day+1, False))# dont buy this one

            memo[(day, holding)] = res 
            return memo[(day, holding)]

        return dp(0, False)

            