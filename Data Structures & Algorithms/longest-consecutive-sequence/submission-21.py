class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        starts = [] 
        longest = 0
        
        for num in numSet:
            if not num - 1 in numSet: 
                starts.append(num)

        for start in starts:
            currNum = start 
            streak = 1 

            while currNum + 1 in numSet: 
                currNum += 1
                streak += 1
 
            longest = max(streak, longest)

        return longest 



            