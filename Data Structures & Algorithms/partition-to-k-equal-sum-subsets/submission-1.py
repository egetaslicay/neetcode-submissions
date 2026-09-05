from functools import cache

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums)

        if total % k != 0: 
            return False 


        target = total // k   ## need to divide for an integer 

        @cache
        def dfs(mask, currSum): 
            if mask  == (1 << n) - 1: 
                return True 

            if currSum == target: 
                return dfs(mask, 0)

            for i in range(n): 

                if (mask & (1 << i)) == 0: 
                    if currSum + nums[i] <= target: 
                        attempt = dfs(mask | (1 << i), currSum + nums[i])
                        if attempt: 
                            return True 
                else: 
                    continue 

            return False

        return dfs(0, 0)

        

            

            





