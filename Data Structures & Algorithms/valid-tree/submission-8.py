class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set() 
        adjacencyMap = defaultdict(list) 

        for edge in edges: 
            a = edge[0]
            b = edge[1]

            adjacencyMap[a].append(b)
            adjacencyMap[b].append(a)

    
        def dfs(node, parent): 
            if node in visited: 
                return False 

            visited.add(node)

            for neighbour in adjacencyMap[node]: 
                if neighbour in visited and neighbour != parent: 
                    return False

                dfs(neighbour, node)


        dfs(0, None)


        for i in range(n): 
            if i not in visited: 
                return False 
        


        return True 

