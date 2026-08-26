class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque() 
        res = [] 
        right = 0 

        while(right < len(nums)):
            curr = nums[right]

            if(queue and right - k == queue[0]): 
                queue.popleft()

            while(queue and curr > nums[queue[-1]]): 
                queue.pop() 
                        
            queue.append(right)

                
            if(right >= k - 1):
                res.append(nums[queue[0]])

            right += 1 


        return res 