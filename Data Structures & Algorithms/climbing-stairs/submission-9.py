class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1 
        if n == 2: return 2 

        
        prev1 = 2
        prev2 = 1

       
        for i in range(3, n+1):
            tempPrev1 = prev1 
            tempPrev2 = prev2 

            prev1 = tempPrev1 + tempPrev2 
            prev2 = tempPrev1


        return prev1