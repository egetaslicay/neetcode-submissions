class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        best = float('-inf')

        for i in range(len(nums)): 

            val = nums[i]   
            best = max(val, best)

            for j in range(i+1, len(nums)): 
                val *= nums[j]
                best = max(val, best)


        return best 

