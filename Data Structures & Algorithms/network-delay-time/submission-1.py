class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacencyList = defaultdict(list)
        distanceMap = {}

        for edge in times: 
            adjacencyList[edge[0]].append((edge[1], edge[2]))

        for i in range(1, n+1): 
            distanceMap[i] = float('inf')

        def dfs(node: int, time: int): 
            if time > distanceMap[node]: 
                return 

            distanceMap[node] = time
            
            for edge in adjacencyList[node]:  
                dest = edge[0]
                add = edge[1]

                dfs(dest, time+add)

        dfs(k, 0)
        res = float('-inf')

        for node, distance in distanceMap.items(): 
            res = max(distance, res)

        if res == float('inf'): 
            return -1 

        return res 

       