class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {} 

        def dp(currSum: int) -> int: 
            if currSum in memo: 
                return memo[currSum]

            if currSum == target: 
                return 1 

            if currSum > target: 
                return 0 

            numWays = 0 

            for num in nums: 
                numWays += dp(currSum + num)
            

            memo[currSum] = numWays 
            return memo[currSum] 

        return dp(0)
