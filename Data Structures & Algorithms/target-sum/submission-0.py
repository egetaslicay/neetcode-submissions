class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {} 

        def recurse(index: int, sumSF: int) -> int: 
            if (index, sumSF) in memo: 
                return memo[(index, sumSF)]

            if index == len(nums):
                if sumSF == target: 
                    return 1 
                else: 
                    return 0 

            count = 0 

            count += recurse(index+1, sumSF + nums[index])
            count += recurse(index+1, sumSF - nums[index])

            memo[(index, sumSF)] = count 
            return memo[(index, sumSF)]

        return recurse(0, 0)  