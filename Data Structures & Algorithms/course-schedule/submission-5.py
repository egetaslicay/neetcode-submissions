class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegreeMap = {}
        nodeToDependents = defaultdict(set)
        numPops = 0 
         
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
                numPops += 1

                for dependent in nodeToDependents[popped]: 
                    indegreeMap[dependent] -= 1 
                    if indegreeMap[dependent] == 0: 
                        ready.append(dependent)

        
        
        if numPops == numCourses: 
            return True
        else: 
            return False 
        