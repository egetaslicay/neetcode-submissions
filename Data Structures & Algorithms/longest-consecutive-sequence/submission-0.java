class Solution {
    public int longestConsecutive(int[] nums) {
        Arrays.sort(nums);
        Map<Integer, Integer> numMap = new HashMap<>(); 
        int keyOfMax = nums[0]; 
        int maxConseq = 1; 
        numMap.put(keyOfMax, 1); 

    
        for(int i = 0; i < nums.length; i++){
            int currNum = nums[i];
            if(numMap.containsKey(currNum-1)){ 
                int temp = numMap.get(currNum - 1); 
                temp++; 
                if(temp > maxConseq){
                    keyOfMax = currNum; 
                    maxConseq = temp; 
                }
                numMap.put(currNum, temp); 
            }
        }
        return maxConseq;
    }
}
