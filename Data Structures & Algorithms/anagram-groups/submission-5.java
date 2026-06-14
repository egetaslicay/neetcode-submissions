class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
    
    Map<String, List<String>> result = new HashMap<>();


     for(String str : strs){ 
     char[] charArray = str.toCharArray(); 
     Arrays.sort(charArray); 
     String sorted = new String(charArray);
     result.putIfAbsent(sorted, new ArrayList<>()); 
     result.get(sorted).add(str); 
     }   

     return new ArrayList<>(result.values()); 


    }
}
