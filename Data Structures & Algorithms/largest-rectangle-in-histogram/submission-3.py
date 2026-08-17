class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxHeight = 0
        
        for i in range(len(heights)): 
            # while theres some kind of 
            while stack and heights[i] < stack[-1][1]: 
                maxHeight = max(maxHeight, stack[-1][1] * (i - stack.pop()[0]))

            stack.append((i, heights[i]))


        return maxHeight



