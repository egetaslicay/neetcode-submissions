class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = [] 
        res.append(intervals[0])

        intervals.sort(key = lambda interval: (interval[0], interval[1]))
        
        for i in range(1, len(intervals)): 
            prevStart, prevEnd = res[-1]
            currStart, currEnd = intervals[i]

            # non overlapping: 
            if prevEnd < currStart:
                res.append(intervals[i])
            # merge: 
            else:
                res[-1] = [min(prevStart, currStart), max(currEnd, prevEnd)] 



        return res 



