class Solution {
    public int maxSubArray(int[] nums) {
        if(nums.length == 0){
            return 0;
        }

    int result = Integer.MIN_VALUE;

    for(int i = 0; i < nums.length; i++){ 
        int currSum = 0;
        for(int j = i; j < nums.length; j++){ 
            currSum += nums[j]; 
            result = Math.max(currSum, result);
        }
    }


    return result;





    }
}
