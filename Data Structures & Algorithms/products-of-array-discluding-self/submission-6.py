class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        for num in nums:
            prod *= nums

        res = []
        for num in nums: 
            res.append(prod / num)
        
        return res 
