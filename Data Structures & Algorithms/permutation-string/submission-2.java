class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if(s2.length() == 0){
            return false;
        }


        // the map for s1
        Map<Character, Integer> s1Map = new HashMap<>(); 
        for(int i = 0; i < s1.length(); i++){ 
            s1Map.put(s1.charAt(i), s1Map.getOrDefault(s1.charAt(i), 0) + 1); 
        } 

        // keep a constant sized window
        int windowSize = s1Map.size(); 


        for(int i = 0; i < s2.length(); i++){ 
        Map<Character, Integer> windowMap = new HashMap<>(); 
        int currWindow = 0; 

        for(int j = i; j < s2.length(); j++){ 
            char c = s2.charAt(j); 
            windowMap.put(c, windowMap.getOrDefault(c, 0)+1); 

            if(s1Map.getOrDefault(c, 0) < windowMap.get(c)){ 
                break; 
            } 

            if(s1Map.getOrDefault(c,0) == windowMap.get(c)){ 
                currWindow++; 
            }

            if(s1Map.keySet().equals(windowMap.keySet())){
                return true;
            }

        }


        }



        return false;

    }
}
