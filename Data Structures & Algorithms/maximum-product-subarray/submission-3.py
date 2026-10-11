class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lo = 1
        hi = 1
        best = float('-inf')

        # at each number we have two choices, either 1, multiply 
        for i in range(len(nums)): 
            lo = min(nums[i] * lo, nums[i])
            hi = max(nums[i] * hi, nums[i])

            best = max(best, hi)

        return best 

