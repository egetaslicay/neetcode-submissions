class Solution {
    public boolean hasDuplicate(int[] nums) {
    Set<Integer> numberSet = new HashSet<>(); 

    for(int i = 0; i < nums.length; i++){ 
        if(!numberSet.contains(nums[i])){ 
            numberSet.add(nums[i]); 
        } else { 
            return true; 
        }
    }  

    return false;
    }
}