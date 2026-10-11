class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lo = 1
        hi = 1
        best = float('-inf')

        # at each number we have two choices, either 1, multiply 
        for x in nums: 
            hi, lo = max(x * hi, x * lo, x), min(x * hi, x * lo, x)
            best = max(best, hi)

        return best 

