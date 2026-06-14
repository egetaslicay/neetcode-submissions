class Solution {
    public boolean checkInclusion(String s1, String s2) {
    if(s1.length() == 0 || s2.length() == 0 || s2.length() < s1.length()){ 
        return false;
    }
    Map<Character, Integer> s1Map = new HashMap<>(); 
    for(int i = 0; i < s1.length(); i++){ 
        s1Map.put(s1.charAt(i), s1Map.getOrDefault(s1.charAt(i), 0)+1);
    }

    for(int i = 0; i < s2.length(); i++){  
        Map<Character, Integer> currMap = new HashMap<>(); 
   
        for(int j = i; j < s2.length(); j++){ 
            char currChar = s2.charAt(j); 
            currMap.put(currChar, currMap.getOrDefault(currChar, 0)+1); 
        
            if(s1Map.getOrDefault(currChar, 0) < currMap.get(currChar)){ 
            break;
            } 

            if(s1Map.equals(currMap)){
            return true;
            }


        }
    }


    return false;
    }
}
