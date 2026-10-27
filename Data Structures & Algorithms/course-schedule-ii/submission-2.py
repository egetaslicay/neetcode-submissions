class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegreeMap = {} 
        nodeToDependents = defaultdict(set) 
        res = [] 

        for i in range(numCourses): 
            indegreeMap[i] = 0

        for edge in prerequisites:
            dependent, preReq = edge 

            if dependent not in nodeToDependents[preReq]: 
                nodeToDependents[preReq].add(dependent)
                indegreeMap[dependent] += 1 


        ready = deque() 

        for node in indegreeMap: 
            if indegreeMap[node] == 0: 
                ready.append(node)


        while ready:
            numPops = len(ready)

            for i in range(numPops): 
                curr = ready.popleft()

                for dependent in nodeToDependents[curr]: 
                    indegreeMap[dependent] -= 1 

                    if indegreeMap[dependent] == 0: 
                        ready.append(dependent)

                res.append(curr)


        if len(res) != numCourses: 
            return [] 

        return res       

        
        

                    
        
