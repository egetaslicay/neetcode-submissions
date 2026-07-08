class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0 

        res = 1
        numSet = set() 
        for num in nums: 
            numSet.add(num)

        for num in numSet: 
            currLength = 1
            if (num-1) in numSet: 
                continue

            curr = num
            while (curr+1) in numSet: 
                currLength += 1
                curr += 1
                res = max(res, currLength)
        
        return res
            