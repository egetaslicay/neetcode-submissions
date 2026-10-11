class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums) 

        for i in range(len(nums)):
            for j in range(i): 
                if nums[j] < nums[i]: 
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

















        
        """
        memo = {} 

        def longest(i: int, prevVal) -> int:
            if i >= len(nums): 
                return 0 

            if (i, prevVal) in memo: 
                return memo[(i, prevVal)]

            length = 0 

            # take 
            if nums[i] > prevVal: 
                length = max(length, 1+longest(i+1, nums[i]))

            # do not take 
            length = max(length, longest(i+1, prevVal))

            memo[(i, prevVal)] = length
            return memo[(i, prevVal)]

        return longest(0, float('-inf'))

        """