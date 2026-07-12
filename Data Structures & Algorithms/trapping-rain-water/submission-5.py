class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = height[0]
        rightMax = height[len(height)-1]
        res = 0 

        left = 0 
        right = len(height)-1
    
        while(left < right): 
            leftMax = max(height[left], leftMax)
            rightMax = max(height[right], rightMax)

            if height[left] < height[right]: 
                currWater = max(0, min(leftMax, rightMax) - height[left])
                left += 1
            else: 
                currWater = max(0, min(leftMax, rightMax) - height[right])
                right -= 1

            res += currWater
        
        return res