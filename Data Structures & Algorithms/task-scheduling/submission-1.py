class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque()    # (release time, count)
        heap = [] 
        counter = Counter(tasks)
        time = 0 



        for task, count in counter.items(): 
            heap.append(-count)

        heapq.heapify(heap)


        while heap or queue:

            # first clear out the heap 
            while queue and queue[0][0] < time: 
                releaseTime, count = queue.popleft() 
                heapq.heappush(heap, count)
            
            if heap: 
                poppedCount = heapq.heappop(heap)
            
                if poppedCount < -1: 
                    queue.append((time + n, poppedCount+1))

            time += 1 

        return time 