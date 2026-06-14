class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length == 0 || nums == null){
            return 0; 
        }

        Set<Integer> numSet = new HashSet<>(); 
        for(Integer num : nums){ 
            numSet.add(num); 
        }

        int longestStreak = 0; 

        for(int num : numSet){ 
            if(!numSet.contains(num-1)){ 
                int curr = num; 
                int streak = 1; 

                while(numSet.contains(curr+1)){ 
                    streak++; 
                    curr++; 
                }

                longestStreak = Math.max(streak, longestStreak);
            }
        }

        return longestStreak;
    }
}
