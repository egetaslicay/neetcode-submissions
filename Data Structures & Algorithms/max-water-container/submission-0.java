class Solution {
    public int maxArea(int[] heights) {
        int maxWater = 0; 

        for(int i = 0; i < heights.length; i++){ 
            for(int j = 0; j < heights.length; j++){
                int width = (j-i);
                int height = Math.min(heights[j], heights[i]);
                int area = width*height; 
                if(area > maxWater){ 
                    maxWater = area; 
                }
            }
        }
        return maxWater;
    }
}
