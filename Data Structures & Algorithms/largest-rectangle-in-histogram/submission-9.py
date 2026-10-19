class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0 
        stack = [] 

        for i in range(len(heights)): 
            extendBack = i

            while stack and stack[-1][0] > heights[i]:
                val, index = stack.pop() 
                res = max(res, val * (i - index))
                extendBack = index

            if stack and stack[-1][0] == heights[i]: 
                continue 
            else: 
                stack.append((heights[i], extendBack))

        for val, index in stack: 
            res = max(res, val * (len(heights)  - index))

        return res 





