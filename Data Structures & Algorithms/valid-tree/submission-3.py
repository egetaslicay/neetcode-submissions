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

        def hasCycle(node: int, parent: int) -> bool: 
            visited.add(node)
            result = False 
            numVisited = 0 

            for neighbour in adjacencyList[node]: 
                if neighbour in visited and not neighbour == parent: 
                    return True 

            for neighbour in adjacencyList[node]: 
                if neighbour not in visited:
                    result = result or hasCycle(neighbour, node)

            return result 

            
        if hasCycle(start, None): 
            return False 


        for i in range(n): 
            if i not in visited: 
                return False


        return True 