class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        heapq.heappush(heap, (0, 0))
        visited = set() 
        total = 0 


        while heap: 
            dist, pointIndex = heapq.heappop(heap)
           
            if len(visited) == len(points): 
                break  

            if pointIndex not in visited: 
                visited.add(pointIndex)
                total += dist 

                for i in range(len(points)): 
                    otherPoint = points[i]
                    currPoint = points[pointIndex] 

                    if i != pointIndex and i not in visited: 
                        distance = abs(otherPoint[0] - currPoint[0]) + abs(otherPoint[1] - currPoint[1])

                        heapq.heappush(heap, (distance, i))
        return total 