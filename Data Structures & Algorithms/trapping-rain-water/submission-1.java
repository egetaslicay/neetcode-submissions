class Solution {
    public int trap(int[] height) {
    int left = 0; 
    int right = height.length-1;
    int leftMax = height[left]; 
    int rightMax = height[right]; 
    int result = 0; 

    while(left < right){ 
        if(leftMax <= rightMax){
            left++;
            result += Math.max(leftMax - height[left], 0);
            leftMax = Math.max(leftMax, height[left]);
            

        } else { 
            right--; 
            result += Math.max(rightMax - height[right], 0);
            rightMax = Math.max(rightMax, height[right]); 
            
        }
    }

    return result;





    }
}
