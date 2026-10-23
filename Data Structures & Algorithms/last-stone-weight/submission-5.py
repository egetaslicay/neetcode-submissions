class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # push everything to a maxHeap 
        heap = [] 
        for stone in stones: 
            heap.append(-1 * stone)

        heapq.heapify(heap)

        # while heap and heap length >= 2: 
        while heap and len(heap) >= 2: 
            stone1 = -1 * heapq.heappop(heap)
            stone2 = -1 * heapq.heappop(heap) 

            difference = max(stone1, stone2) - min(stone1, stone2)

            if difference: # its not zero 
                heapq.heappush(heap, -1 * difference)

        if heap: 
            return -heap[0]

        return 0 


        