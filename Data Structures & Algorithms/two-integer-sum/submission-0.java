class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map <Integer, Integer> indexDiff = new HashMap<>();
        for(int i = 0; i < nums.length; i++){ 
            int diff = target - nums[i]; 
            if(indexDiff.containsKey(nums[i])){
               return new int[] { indexDiff.get(nums[i]), i };
            } else { 
                indexDiff.put(diff, i); 
            }
        }
       return new int[] {};
    }
}
