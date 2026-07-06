class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicti = {} 
        for i, num in enumerate(nums): 
            if num in dicti: 
                return [dicti[num], i]
            else: 
                dicti[target-num] = i
        
        return []