class Solution {
    public boolean hasDuplicate(int[] nums) {
      Set<Integer> seenIntegers = new HashSet<>();
        for(int i = 0; i < nums.length; i++){ 
            if(seenIntegers.contains(nums[i])){
                return true;
            } else { 
                seenIntegers.add(nums[i]); 
            }
        }
        return false;
    }
}