class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        starting = set()
        nums.sort()  # n log n 
        res = [] 
         
        for i in range(len(nums)):
            if nums[i] in starting: 
                continue 

            left = i + 1 
            right = len(nums) - 1

            while left < right: 
                currSum = nums[i] + nums[left] + nums[right]
                
                if currSum < 0: 
                    left += 1 

                elif currSum > 0:
                    right -= 1
                
                else: 
                    res.append([nums[i], nums[left], nums[right]])
                    starting.add(nums[i])
                    left += 1 

                    while nums[left] == nums[left-1] and left < len(nums): 
                        left += 1 

        return res 
                


             

            
