class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        memo = {} 
        
        def dp(i: int, currSum: int) -> bool: 
            if (i, currSum) in memo: 
                return memo[(i, currSum)]

            if total - currSum == currSum: 
                return True 

            if currSum > total //2 or i >= len(nums): 
                return False 

            # either take it or leave it right 
            result = False 

            result = result or dp(i+1, currSum + nums[i])
            result = result or dp(i+1, currSum)

            return result

        return dp(0, 0)
            