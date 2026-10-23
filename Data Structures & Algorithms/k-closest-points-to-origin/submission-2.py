class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] 
        res = [] 



        for point in points: 
            
            distance = point[0]**2 + point[1]**2

            if len(heap) < k: 
                heapq.heappush(heap, (-distance, point))

            else: 
                if -1 * heap[0][0] > distance: 
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-distance, point))
        
        while heap and k > 0:
            res.append(heapq.heappop(heap)[1])

        return res 
            