class Solution {
    public int[] topKFrequent(int[] nums, int k) {
    // base case for empty or zero length array
    if(nums.length == 0 || nums == null){ 
       return null;
    }

    // create frequency map
    Map<Integer, Integer> freqMap = new HashMap<>(); 
    for(int num : nums) { 
        freqMap.put(num,freqMap.getOrDefault(num, 0) + 1);

    }

    // put the entries of the hashmap into a List
    List<Map.Entry<Integer,Integer>> entries = new ArrayList<>(freqMap.entrySet()); 
    entries.sort((a,b) -> b.getValue() - a.getValue());  // sort them in descending orderabstract

    int result[] = new int[k]; // result array should be as big as k.
    for(int i = 0; i < k; i++){ 
    result[i] = entries.get(i).getKey(); 
    }

    return result; 

    }
}
