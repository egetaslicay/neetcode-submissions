class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = 0 
        left = 1 
        right = max(piles) 

        while(left != right):
            mid = left + (right - left)//2 
            timeTaken = 0 

            for pile in piles: 
                timeTaken += math.ceil(pile / mid)

            if(timeTaken > h): 
                left = mid + 1 
                continue 
            else:
                right = mid 

        return left




