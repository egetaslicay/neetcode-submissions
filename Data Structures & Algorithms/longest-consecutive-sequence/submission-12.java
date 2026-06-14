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

    for(int num : numSet){ 
    int streak = 1; 
    int curr = num; 

    if(!numSet.contains(curr-1)){ 
    while(numSet.contains(curr+1)){ 
        streak++; 
        curr++; 
    }
    }

    longest = Math.max(streak, longest); 
    }

    return longest;
    }
}
