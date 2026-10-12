class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = [] 

        for i in range(len(intervals)): 
            curr = intervals[i]

           
            if newInterval[1] < curr[0]: 
                res.append(newInterval)
                return res + intervals[i:]

            elif newInterval[0] > curr[1]: 
                res.append(curr)
                
            else: 
                newStart = min(newInterval[0], curr[0])
                newEnd = max(newInterval[1], curr[1])
                newInterval = [newStart, newEnd]
        
        res.append(newInterval)
        return res 
