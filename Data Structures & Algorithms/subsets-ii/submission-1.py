class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        subset = []

        def backtrack(i: int):
            if i == len(nums): 
                res.append(subset.copy())
                return 

            # take i 
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop() 

            currNum = nums[i]
            i += 1
            
            while i < len(nums) and nums[i] == currNum: 
                i += 1

            backtrack(i)

        nums.sort()     
        backtrack(0)
        return res 

        
             