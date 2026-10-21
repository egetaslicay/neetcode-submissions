class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lo = 1
        hi = 1
        best = float('-inf')

        # at each number we have two choices, either 1, multiply 
        for i in range(len(nums)): 
            negativeCandidate = nums[i] * lo 
            positiveCandidate = nums[i] * hi 


            lo = min(negativeCandidate, nums[i], positiveCandidate)
            hi = max(positiveCandidate, nums[i], negativeCandidate)

            best = max(best, hi)

        return best 
