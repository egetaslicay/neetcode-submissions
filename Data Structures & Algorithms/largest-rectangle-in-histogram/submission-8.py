class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 
        stack = [] 

        for i in range(len(heights)): 
            putIndex = i 

            while stack and heights[i] < stack[-1][1]: 
                height = stack[-1][1]
                backToIndex = stack.pop()[0]
                maxArea = max(maxArea, height * (i - backToIndex)) 
                putIndex = backToIndex 

            stack.append((putIndex, heights[i]))


        for index, height in stack: 
            maxArea = max(maxArea, height * (len(heights) - index))

        return maxArea




