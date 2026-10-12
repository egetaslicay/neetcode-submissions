"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda e: (e.start, e.end))
        heap = []
        res = 0 

        for i in range(len(intervals)): 
            curr = intervals[i]
            # while the start of the current meeting is >= to the top of the heap and stack exists pop the heap 
            # push the end time of this meeting into the heap 
            # res = max(res, len(heap))

            while heap and curr.start >= heap[0]: 
                heapq.heappop(heap)

            heapq.heappush(heap, curr.end)
            res = max(res, len(heap))

        return res 