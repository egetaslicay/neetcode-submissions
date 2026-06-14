class Solution {
    public int maxArea(int[] heights) {
        int maxWater = 0; 
        int l = 0; 
        int r = heights.length-1; 

    while(l < r){ 
        int w = (r - l); 
        int h = Math.min(heights[l], heights[r]); 
        int currWater = w*h; 
        if(currWater > maxWater){
            maxWater = currWater;
        }
        if(Math.min(heights[l], heights[r]) == heights[l]){ 
            l++;
        } else  {
            r--; 
        }

    }

    return maxWater;
    }
}
