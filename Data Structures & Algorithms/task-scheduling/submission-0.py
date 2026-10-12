class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        freqMap = Counter(tasks)
        heap = [] 
        
        for letter, count in freqMap.items(): 
            heap.append(-count)

        heapq.heapify(heap)

        cooldown = deque() 
        
        while heap or cooldown: 
            time += 1 

            if heap: 
                poppedVal = heapq.heappop(heap) # some negative number 

                if abs(poppedVal) > 1: 
                    cooldown.append((time + n, poppedVal + 1))

            if cooldown and cooldown[0][0] <= time: 
                    popped = cooldown.popleft()
                    heapq.heappush(heap, popped[1])
        

        return time 