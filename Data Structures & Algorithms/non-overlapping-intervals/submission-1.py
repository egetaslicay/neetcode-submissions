class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda interval: (interval[0], interval[1]))
        prev = intervals[0]
        count = 0 

        for i in range(1, len(intervals)): 
            curr = intervals[i]
       
            if prev[1] > curr[0]:
                count += 1

                if curr[1] < prev[1]: 
                    prev = curr 
                    
            else: 
                prev = curr 


        return count 