class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges: 
            return True 


        visited = set()
        adjacencyList = defaultdict(list)

        for edge in edges: 
            a = edge[0]
            b = edge[1]

            adjacencyList[a].append(b)
            adjacencyList[b].append(a)

        start = edges[0][0]

        def dfs(node: int) -> bool: 
            visited.add(node)
            result = False 
            numVisited = 0 

            for neighbour in adjacencyList[node]: 
                if neighbour in visited: 
                    numVisited += 1

            if numVisited >= 2: 
                return True 

            for neighbour in adjacencyList[node]: 
                if neighbour not in visited:
                    result = result or dfs(neighbour)

            return result 

            
        if dfs(start): 
            return False 


        for i in range(n): 
            if i not in visited: 
                return False


        return True 