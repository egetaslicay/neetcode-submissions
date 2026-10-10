class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {}
        nodeToDependents = defaultdict(set) 
        poppedCount = 0 


        for group in prerequisites:
            preReq = group[1]
            dependent = group[0]

            if preReq not in indegree:
                indegree[preReq] = 0 

            if dependent not in indegree: 
                indegree[dependent] = 0

            if dependent not in nodeToDependents[preReq]: 
                indegree[dependent] += 1
                nodeToDependents[preReq].add(dependent)

        queue = deque()

        for node in indegree: 
            if indegree[node] == 0: 
                queue.append(node)

        while queue: 
            node = queue.popleft()
            poppedCount += 1

            for dependent in nodeToDependents[node]:
                if indegree[dependent] == 1: 
                    queue.append(dependent)

                indegree[dependent] -= 1

        return poppedCount == len(indegree)

                    
        
