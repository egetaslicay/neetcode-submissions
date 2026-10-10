class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0 
        visited = set() 
        adjacencyList = defaultdict(list)

        for edge in edges: 
            a = edge[0]
            b = edge[1]
            
            adjacencyList[a].append(b)
            adjacencyList[b].append(a)


        def dfs(node: int): 
            if node in visited: 
                return 

            visited.add(node)

            for neighbour in adjacencyList[node]: 
                dfs(neighbour)

        
        for i in range(n): 
            if i not in visited: 
                count += 1 
                dfs(i)


        return count 