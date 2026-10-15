class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        combo = [] 

        def dfs(i, sumLeft): 
            if sumLeft == 0: 
                res.append(combo.copy())
                return 

            if i >= len(nums) or sumLeft < 0: 
                return 

            # we can either take another one of this one or move on: 
            combo.append(nums[i])
            dfs(i, sumLeft - nums[i])
            combo.pop() 
            dfs(i + 1, sumLeft)

        dfs(0, target)
        return res 


