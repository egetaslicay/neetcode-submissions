class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxHeight = 0
        
        for i in range(len(heights)): 
            # while theres some kind of 
            putIndex = 0

            while stack and heights[i] < stack[-1][1]: 
                height = stack[-1][1]
                putIndex = stack.pop()[0]
                maxHeight = max(maxHeight, height * (i - putIndex))

            stack.append((putIndex, heights[i]))

        for index, height in stack: 
            maxHeight = max(maxHeight, height * (len(heights) - index))


        return maxHeight



