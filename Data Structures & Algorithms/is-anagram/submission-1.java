class Solution {
    public boolean isAnagram(String s, String t) {
    if(s.length() != t.length()){
        return false;
    }

    Map<Character, Integer> letterFreqS = new HashMap<>(); 
    Map<Character, Integer> letterFreqT = new HashMap<>(); 

    // fill out charachter frequency map 
    for(int i = 0; i < s.length(); i++){ 
        char sLetter = s.charAt(i); 
        char tLetter = t.charAt(i); 
        letterFreqS.put(sLetter, letterFreqS.getOrDefault(sLetter,0) + 1);
        letterFreqT.put(tLetter, letterFreqT.getOrDefault(tLetter, 0) + 1);
    }

    return letterFreqS.equals(letterFreqT); 
    }
}
