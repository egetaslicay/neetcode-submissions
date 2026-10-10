class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjacencyList = defaultdict(list) 

        def canReach(curr: int, target: int, visited: set) -> boolean: 
            if curr == target: 
                return True

            visited.add(curr)
            result = False

            for neighbour in adjacencyList[curr]: 
                if neighbour not in visited: 
                    result = result or canReach(neighbour, target, visited)

            return result 



        for edge in edges: 
            visited = set() 
            a = edge[0]  
            b = edge[1]

            if canReach(a, b, visited): 
                return edge 

            adjacencyList[a].append(b)
            adjacencyList[b].append(a)

        return [] 