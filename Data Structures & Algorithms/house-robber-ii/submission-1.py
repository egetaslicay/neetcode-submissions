class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]


        def robline(houses: List[int]) -> int: 
            memo = {} 

            def recurse(index: int): 
                if index in memo: 
                    return memo[index]
                    
                if index >= len(houses): 
                    return 0 

                memo[index] = max(houses[index] + recurse(index + 2), recurse(index+1)) 

                return memo[index]


            return recurse(0) 


        return max(robline(nums[1:]), robline(nums[:-1]))
                




