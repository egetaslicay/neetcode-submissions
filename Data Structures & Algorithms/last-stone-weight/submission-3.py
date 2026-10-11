class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [] 

        for stone in stones: 
            heapq.heappush(heap, -1 * stone)

        while len(heap) >= 2: 
            elem1 = -1 * heapq.heappop(heap)
            elem2 = -1 * heapq.heappop(heap)

            if elem1 != elem2: 
                heapq.heappush(heap,  -1*abs(elem1-elem2))

        if not heap: 
            return 0 
        
        return heap[0] * -1 



        