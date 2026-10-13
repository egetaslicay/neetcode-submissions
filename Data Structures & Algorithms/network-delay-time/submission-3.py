class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacencyList = defaultdict(list)
        distanceMap = {}

        for edge in times: 
            adjacencyList[edge[0]].append((edge[1], edge[2]))

        for i in range(1, n+1): 
            distanceMap[i] = float('inf')

        heap = []
        heapq.heappush(heap, (0,k))

        while heap:
            dist, node =  heapq.heappop(heap)
             
            if distanceMap[node] == float('inf'): 
                distanceMap[node] = dist

                for edge in adjacencyList[node]:
                    edgeNode, edgeDist = edge
                     
                    heapq.heappush(heap, (edgeDist + dist, edgeNode))

        res = float('-inf')

        for node, distance in distanceMap.items(): 
            res = max(distance, res)

        if res == float('inf'): 
            return -1 

        return res 
            


        