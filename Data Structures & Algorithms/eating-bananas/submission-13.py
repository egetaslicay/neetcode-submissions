class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = math.ceil(sum(piles) / h)

        while(left < right): 
            mid = (right + left) // 2
            currHours = 0 

            for pile in piles: 
                currHours += math.ceil(pile / mid)
            
            if currHours <= h: 
                right = mid 
            else: 
                left = mid + 1


        return left 






