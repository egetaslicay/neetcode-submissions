class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {} 

        def longest(i: int, prevVal) -> int:
            if i >= len(nums): 
                return 0 

            if nums[i] <= prevVal: 
                return 0 

            if (i, prevVal) in memo: 
                return memo[(i, prevVal)]

            length = 0 

            # take 
            length = max(length, 1+longest(i+1, nums[i]))
            # do not take 
            length = max(length, longest(i+1, prevVal))

            memo[(i, prevVal)] = length
            return memo[(i, prevVal)]

        return longest(0, float('-inf'))