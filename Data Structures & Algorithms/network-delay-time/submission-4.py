class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distanceMap = defaultdict(int) 
        adjacencyMap = defaultdict(list)
        heap = [] 

        for source, target, cost in times:
            adjacencyMap[source].append((cost, target))

        heapq.heappush(heap, (0, k))


        while heap: 
            distanceSF, currNode = heapq.heappop(heap)

            if currNode in distanceMap: 
                continue 
            
            distanceMap[currNode] = distanceSF 

            for cost, neighbour in adjacencyMap[currNode]: 
                if neighbour not in distanceMap: 
                    heapq.heappush(heap, (distanceSF + cost, neighbour))



        for i in range(1, n+1): 
            if i not in distanceMap: 
                return -1

        return max(distanceMap.values()) 
            

        