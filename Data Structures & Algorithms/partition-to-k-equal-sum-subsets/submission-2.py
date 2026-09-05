from functools import cache

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums)

        memo = {} 

        if total % k != 0: 
            return False 


        target = total // k   ## need to divide for an integer 

        def dfs(mask, currSum): 
            if mask in memo: 
                return memo[mask]

            if mask  == (1 << n) - 1:
                memo[mask] = True
                return True 

            if currSum == target: 
                return dfs(mask, 0)

            for i in range(n): 

                if (mask & (1 << i)) == 0: 
                    if currSum + nums[i] <= target: 
                        attempt = dfs(mask | (1 << i), currSum + nums[i])
                        if attempt: 
                            memo[mask] = True
                            return True 
                else: 
                    continue 

            memo[mask] = False
            return False

        return dfs(0, 0)

        

            

            





