class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda interval: (interval[0], interval[1]))

        prev = intervals[0]
        count = 0 

        for i in range(1, len(intervals)):
            prevStart, prevEnd = prev 
            currStart, currEnd = intervals[i]

            if prevEnd <= currStart: 
                prev = intervals[i]
            else: 
                count += 1
                if currEnd < prevEnd: 
                    prev = intervals[i]

        return count 