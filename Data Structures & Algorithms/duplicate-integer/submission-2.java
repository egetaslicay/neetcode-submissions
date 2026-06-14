class Solution {
    public boolean hasDuplicate(int[] nums) {
    if(nums.length == 0 || nums == null){
        return false;
    }

    Set<Integer> numSet = new HashSet<>(); 

    for(int i = 0; i < nums.length; i++){ 
    if(numSet.contains(nums[i])){
        return true;
    } else { 
        numSet.add(nums[i]);
    }
}

return false;

      
    }
}