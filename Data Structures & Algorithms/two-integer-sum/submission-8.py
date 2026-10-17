class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookingForToIndex = {} 

        for i in range(len(nums)): 
            if nums[i] in lookingForToIndex: 
                return [lookingForToIndex[nums[i]], i]
            else: 
                lookingForToIndex[target-nums[i]] = i 

        return [] 