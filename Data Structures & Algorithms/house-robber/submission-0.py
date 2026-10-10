class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robMaxxing(i: int) -> int: 
            if i >= len(nums): 
                return 0 

            robVal = nums[i] + robMaxxing(i+2)
            skipVal = 0 + robMaxxing(i+1)

            return max(robVal, skipVal)


        return robMaxxing(0)

