"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda interval: (interval.start, interval.end))

        prev = intervals[0]

        for i in range(1, len(intervals)): 
            
            curr = intervals[i]

            if curr.start >= prev.end: 
                prev = intervals[i]

            else: 
                return False 

        return True 