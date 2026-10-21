class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegreeMap = {}
        nodeToDependents = defaultdict(set)
        res = [] 
         
        for i in range(numCourses): 
            indegreeMap[i] = 0 

        
        for dependent, preReq in prerequisites: 

            if dependent not in nodeToDependents[preReq]: 
                indegreeMap[dependent] += 1 
                nodeToDependents[preReq].add(dependent)

        ready = deque()

        for node, indegree in indegreeMap.items(): 
            if indegree == 0: 
                ready.append(node)


        while ready: 
            numPops = len(ready)

            for i in range(numPops):
                popped = ready.popleft()
                res.append(popped)

                for dependent in nodeToDependents[popped]: 
                    indegreeMap[dependent] -= 1 
                    if indegreeMap[dependent] == 0: 
                        ready.append(dependent)

        
        
        if len(res) == numCourses: 
            return res
        else: 
            return []
        

                    
        
