class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<String, Integer> stringMap1 = new HashMap<>();
        HashMap<String, Integer> stringMap2 = new HashMap<>(); 
        
        if(s.length() != t.length()){
            return false;
        }

        for(int i = 0; i < s.length(); i++){
            if(!stringMap1.containsKey(s.substring(i, i+1))){ 
                stringMap1.put(s.substring(i, i+1), 1); 
            } else { 
                int temp = stringMap1.get(s.substring(i,i+1)); 
                temp += 1; 
                stringMap1.put(s.substring(i,i+1), temp);
            }

            if(!stringMap2.containsKey(t.substring(i, i+1))){ 
                stringMap2.put(t.substring(i, i+1), 1); 
            } else { 
                int temp = stringMap2.get(t.substring(i,i+1)); 
                temp += 1; 
                stringMap2.put(t.substring(i,i+1), temp);
            }
        }

        return stringMap1.equals(stringMap2);

    }
}
