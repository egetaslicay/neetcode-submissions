class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {}
        nodeToDependents = defaultdict(set) 
        poppedCount = 0 


        for group in prerequisites: 
            dependency = group[0]
            dependents = group[1:]

            if not dependency in indegree:
                indegree[dependency] = 0 

            for dependent in dependents: 
                if not dependent in indegree: 
                    indegree[dependent] = 0 

                if not dependent in nodeToDependents[dependency]: 
                    nodeToDependents[dependency].add(dependent)
                    indegree[dependent] += 1
        
        ready = [] 

        for node in indegree: 
            if indegree[node] == 0: 
                ready.append(node)

        while ready: 
            prevReady = ready.copy() 
            ready = [] 

            for node in prevReady: 
                poppedCount += 1

                for dependent in nodeToDependents[node]:
                    if indegree[dependent] == 1: 
                        ready.append(dependent)

                    indegree[dependent] -= 1

        return poppedCount == len(indegree)

                    
        
