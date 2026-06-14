class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> sortedThenList = new HashMap<>(); 

        for(int i = 0; i < strs.length; i++){ 
        char[] chars = strs[i].toCharArray();
        Arrays.sort(chars);
        String sorted = new String(chars);

        if(!sortedThenList.containsKey(sorted)){ 
            sortedThenList.put(sorted, new ArrayList<>());
            sortedThenList.get(sorted).add(strs[i]);
        } else { 
            List<String> temp = sortedThenList.get(sorted);
            temp.add(strs[i]); 
        }
        }
        return new ArrayList<>(sortedThenList.values());
    }
}
