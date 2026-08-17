class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left + 1
        res = 0

        while(left <= right and right < len(prices)): 
            res = max(res, prices[left] - prices[right])

            while(prices[left] > prices[right]): 
                left += 1

            right += 1

        return res 