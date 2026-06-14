class Solution {
    public int singleNumber(int[] nums) {
        Set<Integer> numSet = new HashSet<>(); 

        for(int i = 0; i < nums.length; i++){ 
            if(!numSet.contains(nums[i])){
                numSet.add(nums[i]); 
            } else {
                numSet.remove(nums[i]); 
            }
        }
        return numSet.iterator().next();
    }
}
