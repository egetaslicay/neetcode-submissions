class Solution {
    public int trap(int[] height) {
    int left = 0;
    int right = height.length-1; 

    int leftMax = height[0]; 
    int rightMax = height[height.length-1]; 
    int result = 0; 

    while(left < right){ 
        if(leftMax <= rightMax){ 
            left++; 
            result += Math.max(0,leftMax - height[left]);
            leftMax = Math.max(leftMax, height[left]); 
            
        } else { 
            right--; 
            result +=  Math.max(0, rightMax - height[right]);
            rightMax = Math.max(rightMax, height[right]); 
             // no need to take minimum of either side.
        }
    }


    return result;
    }
}
