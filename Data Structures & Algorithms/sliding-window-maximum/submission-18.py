class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []  
        
        for i in range(k):
            heap.append((-nums[i], i))

        heapq.heapify(heap)
        res.append(heap[0][0] * -1)


        for right in range(k, len(nums)): 
            heapq.heappush(heap, (nums[right] * -1, right))

            if heap[0][1] > right - k: 
                res.append(heap[0][0] * -1)
            else: 
                while heap and heap[0][1] <= right - k:
                    heapq.heappop(heap)
                
                res.append(heap[0][0] * -1)

        return res 

