class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myCounter = Counter(nums)
        heap = []   
        res = [] 

        for element, count in myCounter.items(): 
            heap.append((-count, element))

        heapq.heapify(heap)
        
        while heap and k > 0:
            count, element = heapq.heappop(heap)
            res.append(element)
            k -= 1

        return res 



