class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> numFreq = new HashMap<>(); 

        for(int i = 0; i < nums.length; i++){ 
            if(!numFreq.containsKey(nums[i])){
                numFreq.put(nums[i], 1); 
            } else { 
                int temp = numFreq.get(nums[i]); 
                temp++; 
                numFreq.put(nums[i], temp);
            }
        }

        List<Map.Entry<Integer, Integer>> entries = new ArrayList<>(numFreq.entrySet());
        entries.sort((a, b) -> b.getValue() - a.getValue()); 

        int[] result = new int[k];
        for(int i = 0; i < k; i++){ 
            result[i] = entries.get(i).getKey();
        }

        return result; 
    }
}
