class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda e: (e[0], e[1]))
        res = [] 
        
        for query in queries:
            bestLength = float('inf') 

            for interval in intervals: 
                if query <= interval[1] and query >= interval[0]: 
                    bestLength = min(bestLength, interval[1] - interval[0] + 1)

            if bestLength == float('inf'): 
                res.append(-1)
            else: 
                res.append(bestLength)

        return res 