class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
    List<Integer> result = new ArrayList<>(); 

    for(int i = 0; i <= nums.length - k; i++){ 
        int maxInWindow = nums[i];
        for(int j = i; j < i + k; j++){ 
        maxInWindow = Math.max(nums[j], maxInWindow); 
        }

        result.add(maxInWindow);
    }

    int actualResult[] = new int[result.size()];
    for(int i = 0; i < result.size(); i++){
        actualResult[i] = (int) result.get(i);       
    }

    return actualResult;



    }
}
