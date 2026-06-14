class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
    
    Map<String, List<String>> charMap = new HashMap<>(); 

    for(String s : strs){ 
        char[] charArray = s.toCharArray(); 
        Arrays.sort(charArray); 
        String sortedString = new String(charArray); 
        charMap.putIfAbsent(sortedString, new ArrayList<>()); 
        charMap.get(sortedString).add(s); 
    }

    return new ArrayList<>(charMap.values()); 


    }
}