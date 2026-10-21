class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjacencyList = defaultdict(list)
        
        def canReach(curr, target, visited): 
            if curr == target: 
                return True 

            visited.add(curr)
            result = False 

            for neighbour in adjacencyList[curr]: 
                if neighbour not in visited: 
                    result = result or canReach(neighbour, target, visited)

            return result 


        for a, b in edges: 
            if canReach(a, b, set()):  # do we already have an edge that lets us get to the other one 
                return [a, b]
            else: 
                adjacencyList[a].append(b)
                adjacencyList[b].append(a) 

            
        

        



