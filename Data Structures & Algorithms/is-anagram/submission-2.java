class Solution {
    public boolean isAnagram(String s, String t) {
       if(s.length() != t.length()){ 
        return false; 
       }

       Map<Character, Integer> charMapS = new HashMap<>(); 
       Map<Character, Integer> charMapT = new HashMap<>(); 

       for(int i = 0; i < s.length(); i++){ 
       char sChar = s.charAt(i); 
       char tChar = t.charAt(i); 

       charMapS.put(sChar, charMapS.getOrDefault(sChar, 0) + 1); 
       charMapT.put(tChar, charMapT.getOrDefault(tChar, 0) + 1); 
       }

        return charMapS.equals(charMapT); 


    }
}
