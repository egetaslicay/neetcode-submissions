class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length == 0 || nums == null){
            return 0; 
        } 


        Set<Integer> numSet = new HashSet<>(); 
        for(int num : nums){ 
            numSet.add(num); 
        }

        int longest = 0; 
        for(int num : numSet) { 
            if(!numSet.contains(num-1)){ 
                int current = num;
                int streak = 1; 
                
                while(numSet.contains(current+1)){ 
                    streak++;
                    current++;
                }    

                 longest = Math.max(streak, longest); 
            }

           
        }

        return longest;
    }
}
