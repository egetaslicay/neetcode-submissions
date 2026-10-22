"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda a: (a.start, a.end))
        heap = []
        minimumRooms = float('-inf')
        
        for i in range(len(intervals)): 
            curr = intervals[i]

            # remove all the ended meetings 
            while heap and heap[0] <= curr.start: 
                heapq.heappop(heap)

            heapq.heappush(heap, curr.end)
            minimumRooms = max(minimumRooms, len(heap))

        return minimumRooms 


    #  intervals=[(0,40),(5,10),(15,20)]                    
    #  curr = (0,40) 
    #  
            

            
        
