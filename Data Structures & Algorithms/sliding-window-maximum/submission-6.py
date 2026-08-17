class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [] 

        left = 0
        right = 0

        queue = deque() # contains indices ?? since we can map with nums[]

        
        while(right < len(nums)): 
            # pop all numbers smaller since we are adding a nice large number
            while queue and nums[queue[-1]] < nums[right]: 
                queue.pop()
            queue.append(right)
            
            # remove left value from the window 
            if left > queue[0]: 
                queue.popleft()

            if (right + left) >= k: 
                res.append(nums[queue[0]])
                left += 1
            right += 1 
        
        return res



