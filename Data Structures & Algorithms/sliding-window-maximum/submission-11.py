class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = [] 
        q = deque()
        right = 0 


        # initial fill from 0 to k-1 
        while right in range(k): 
            # get rid of everything SMALLER then put it in its place 
            while q and nums[right] > nums[q[-1]]: 
                q.pop() 
            q.append(right)
            
        output.append(q[0])


        # start at k 
        for r in range(k, len(nums)): 

            while q and nums[right] > nums[q[-1]]:
                q.pop() 
            q.append(right)

            # remove the now old 
            if q[0] <= right - k: 
                q.popleft() 

            output.append(q[0])
            r += 1

        return output