class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {} 
        
        def recursive(index: int) -> int:
            if index in memo: 
                return memo[index]
                
            if index >= len(cost): 
                return 0 

            return cost[index] + min(recursive(index+1),recursive(index+2))

    
        return min(recursive(0), recursive(1)) 
        