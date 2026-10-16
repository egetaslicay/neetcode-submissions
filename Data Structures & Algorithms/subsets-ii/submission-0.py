class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        subset = []

        def backtrack(i: int):
            if i == len(nums)-1: 
                res.append(subset.copy())
                return 

            # take i 
            subset.append(nums[i])
            dfs(i+1)
            subset.pop() 

            currNum = nums[i]
            i += 1
            
            while i < len(nums) and nums[i] == currNum: 
                i += 1

            dfs(i)
            
        
        nums.sort() 
        return res 

        
             