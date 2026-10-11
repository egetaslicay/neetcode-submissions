class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distancePointHeap = [] 
        res = []

        for point in points: 
            val1, val2 = point

            distance = val1**2 + val2**2 
            distancePointHeap.append((distance, val1, val2))

        
        heapq.heapify(distancePointHeap)



        while distancePointHeap and k > 0: 
            k -= 1 
            distance, val1, val2 = heapq.heappop(distancePointHeap)
            res.append([val1, val2])


        return res 