class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0 
        numSet = set() 
        for num in nums: 
            numSet.add(num)

        for num in numSet: 
            currLength = 1
            if (num-1) in numSet: 
                continue

            curr = num
            while (curr+1) in numSet: 
                curr += 1
                currLength += 1
                res = max(res, currLength)
        
        return res
            