class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = {}
        nodeToDependents = defaultdict(set) 
        res = [] 

        for i in range(numCourses): 
            indegree[i] = 0 

        for group in prerequisites:
            preReq = group[1]
            dependent = group[0]

            if dependent not in nodeToDependents[preReq]: 
                indegree[dependent] += 1
                nodeToDependents[preReq].add(dependent)
        
        ready = [] 

        for node in indegree: 
            if indegree[node] == 0: 
                ready.append(node)

        while ready: 
            prevReady = ready.copy() 
            ready = [] 
            
            for node in prevReady: 
                res.append(node)

                for dependent in nodeToDependents[node]:
                    if indegree[dependent] == 1: 
                        ready.append(dependent)

                    indegree[dependent] -= 1
        

        if len(res) != numCourses: 
            return [] 

        return res

                    
        
