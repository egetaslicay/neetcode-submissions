class Solution {
    public int[] productExceptSelf(int[] nums) {
    if(nums.length == 0 || nums == null){ 
        return new int[]{};
    }

    int[] result = new int[nums.length]; 
    
    for(int i = 0; i < nums.length; i++){ 
    
    int self = nums[i]; 
    int prod = 1; 

    for(int j = 0; j < nums.length; j++){ 
        if(nums[j] != self && j != i){ 
        prod *= nums[j]; 
        }
    }

    result[i] = prod;
    }

    return result;
        
    }
}  
