class Solution:
    def rob(self, nums: List[int]) -> int: 
        memo = {} 
        
        def robMaxxing(i: int) -> int:
            if i in memo: 
                return memo[i] 

            if i >= len(nums): 
                return 0 

            robVal = nums[i] + robMaxxing(i+2)
            skipVal = 0 + robMaxxing(i+1)

            memo[i] = max(robVal, skipVal)
            return memo[i]


        return robMaxxing(0)

