class Solution {
    public int maxArea(int[] heights) {
        int maxWater = 0;

        int left = 0; 
        int right = heights.length-1;

        while(left < right) { 
        int width = (right - left); 
        int height = Math.min(heights[right], heights[left]); 
        int currWater = width * height;

        maxWater = Math.max(maxWater, currWater); 
        if(heights[right] < heights[left]){ 
            right--; 
        } else if(heights[right] > heights[left]){ 
            left++;
        } else { 
            right--; 
        }
    }

    return maxWater;




    }
}
