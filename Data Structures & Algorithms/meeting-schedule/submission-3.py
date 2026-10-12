"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: 
            return True 
            
        intervals.sort(key = lambda e: (e.start, e.end))

        prev = intervals[0] 

        for i in range(1, len(intervals)): 
            curr = intervals[i]


            # the start of prev will always be before or @ the same time as the start of curr 
            # the way we check if theres an overlap is if prev[1] > curr[0] 

            #     |--------|  curr
            #   |--------| or -----| 

            if prev.end > curr.start: 
                return False
            
            prev = curr 

        return True 