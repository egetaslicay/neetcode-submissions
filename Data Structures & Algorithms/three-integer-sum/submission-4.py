class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        firstSet = set()
        res = []


        for i in range(len(nums)-1): 
            if nums[i] in firstSet:
                continue
        
            firstSet.add(nums[i])
            l = i + 1
            r = len(nums)-1

            while(l < r): 
                if nums[i] + nums[l] + nums[r] > 0: 
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0: 
                    l += 1
                else: 
                    res.append([nums[i], nums[l] , nums[r]])
                    l += 1
                    r -= 1
        
    
        return res





