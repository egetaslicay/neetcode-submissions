class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> diffIndex = new HashMap<>(); 

        for(int i = 0; i < nums.length; i++){ 
            int diff = target - nums[i];
            if(diffIndex.containsKey(nums[i])){ 
                return new int[] { diffIndex.get(nums[i]), i}; 
            } else { 
                diffIndex.put(diff, i);
            }
        }


         return new int[] {}; 
    }
}
