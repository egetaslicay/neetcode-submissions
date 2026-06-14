class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numberSet = new HashSet<>(); 
        for(int num : nums){ 
            numberSet.add(num); 
        }

        int longestSeq = 0; 

        for (int num : numberSet){ 
            if(!numberSet.contains(num -1)){ 
                int length = 1; 
                int currNum = num; 
                while(numberSet.contains(currNum + 1)){
                    currNum++; 
                    length++; 
                }
                if(length > longestSeq){
                    longestSeq = length; 
                }
            }
        }


        return longestSeq;

    }
}
