class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
    HashSet<List<Integer>> set = new HashSet<>();
    
    for(int i  = 0; i < nums.length; i++){ 
        for(int j = 0; j < nums.length; j++){
            for(int k = 0; k < nums.length; k++){
                if(i != j && i != k && k!= j){
                    if(nums[i] + nums[j] + nums[k] == 0){
                        ArrayList<Integer> triplet = new ArrayList<>(); 
                        triplet.add(nums[i]);
                        triplet.add(nums[j]);
                        triplet.add(nums[k]);
                        Collections.sort(triplet);

                        set.add(triplet);
                    }
                }       
            }
        }
    }
    ArrayList<List<Integer>> list = new ArrayList<>(set); 
    return list;
    }
}
