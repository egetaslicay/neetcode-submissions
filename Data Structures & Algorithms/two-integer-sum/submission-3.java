class Solution {
    public int[] twoSum(int[] nums, int target) {
        if(nums.length == 0){ 
            return null; 
        }
        Map<Integer, Integer> neededNumber = new HashMap<>(); 

        for(int i = 0; i < nums.length; i++) {   
            if(neededNumber.containsKey(nums[i])){ 
            return new int[] { neededNumber.get(nums[i]), i };
            } else { 
                int difference = target - nums[i]; 
                neededNumber.put(difference, i); 
            }

          
        }

        return null; 

        /// check if the hashmap has this number as the key first, if it does, return the index you are currently at and the value 
        // associated with this key, if not, take the difference of target - number you are currently at and then value as the index you 
        // are currently at

    }
}
