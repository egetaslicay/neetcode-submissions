class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort(key = lambda interval: (interval[0], interval[1]))

        res.append(intervals[0])

        for i in range(1, len(intervals)): 
            curr = intervals[i]

            if res[-1][1] < curr[0]: # res[-1] is completely before curr
                res.append(curr)  # add curr to res it becomes the new end of the list
            else:  # res[-1] is merged with this one update res[-1]
                prev = res[-1]
                newEnd = max(prev[1], curr[1])
                res[-1] = [prev[0], newEnd]

        return res 