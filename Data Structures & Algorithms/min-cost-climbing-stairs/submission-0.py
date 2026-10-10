class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def recursive(index: int) -> int:
            if index >= len(cost): 
                return 0 


            return min(cost[index] + recursive(index+1), cost[index] + recursive(index+2))

    
        return min(recursive(0), recursive(1)) 
        