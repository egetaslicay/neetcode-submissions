class Solution {
    public int trap(int[] height) {
    int[] leftMaxes = new int[height.length]; 
    int[] rightMaxes = new int[height.length]; 
    int result = 0; 

    int leftMax = height[0]; 
   
    for(int i = 0; i < height.length; i++){ 
        leftMaxes[i] = leftMax;
        leftMax = Math.max(leftMax, height[i]); 
    }

    int rightMax = height[height.length-1];

    for(int i = height.length-1; i > 0; i--){ 
        rightMaxes[i] = rightMax;
        rightMax = Math.max(rightMax, height[i]); 
    }

    for(int i = 0; i < height.length; i++){ 
        result += Math.max(0, Math.min(leftMaxes[i], rightMaxes[i]) - height[i]);
    }

    return result; 


    }
}
