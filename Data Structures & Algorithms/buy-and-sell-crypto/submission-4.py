class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSF = prices[0]
        maxP = 0 

        for price in prices: 
            maxP = max(maxP, price - minSF)
            minSF = min(minSF, price)

        return maxP