class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        firstSet = set()
        res = []


        for i in range(len(nums)): 
            if nums[i] in firstSet:
                continue
        
            firstSet.add(nums[i])
            l = i + 1
            r = len(nums)-1

            while(l < r): 
                sum = nums[i] + nums[l] + nums[r]
                if sum > 0: 
                    r -= 1
                elif sum < 0: 
                    l += 1
                else: 
                    res.append([nums[i], nums[l] , nums[r]])
                    l += 1
                    r -= 1
        
    
        return res





