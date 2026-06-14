class Solution {
    public int missingNumber(int[] nums) {
        Set<Integer> numSet = new HashSet<>(); 

        for(int i = 0; i < nums.length; i++){ 
            numSet.add(nums[i]); 
        }
        

        for(int j = 0; j <= numSet.size(); j++){ 
            if(!numSet.contains(j)){ 
                return j;
            }
        }
        return 0;
    }
}

