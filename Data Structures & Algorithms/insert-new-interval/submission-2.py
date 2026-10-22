class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        curr = newInterval 
        res = [] 

        for i in range(len(intervals)): 
            start, end = intervals[i]
            currStart, currEnd = curr

            
            # non overlapping first
            if end < currStart or currEnd < start: 
                # interval at i is strictly after curr 
                if currEnd < start: 
                    res.append(curr)     
                    curr = intervals[i]

                # curr is strictly after the interval at i    
                else:
                    res.append(intervals[i])

            # overlapping intervals 
            else: 
                curr = [min(currStart, start), max(currEnd, end)] 

        
        # if you havent added curr yet add it at the end 
        if not res or res[-1] != curr: 
            res.append(curr)

        return res 