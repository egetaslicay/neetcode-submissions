class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [] # List[List[int]]

        currSubset = [] # subset we are currently working on 

        def dfs(i: int): 
            if i >= len(nums): 
                result.append(currSubset.copy()) # im not sure what this does tbh 
                return 

          

            # we want to add branch 
            currSubset.append(nums[i])
            dfs(i + 1)

            # do not add branch 
            currSubset.pop()
            dfs(i + 1)
        
        dfs(0)

        return result