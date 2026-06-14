class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] productArray = new int[nums.length]; 
        for(int i = 0; i < nums.length; i++){ 
             int prod = 1; 
            for(int j = 0; j < nums.length; j++){
                if(j == i){
                    continue;
                } else { 
                   prod = prod * nums[j]; 
                }
            }
            productArray[i] = prod;
        }
        return productArray;
    }
}  
