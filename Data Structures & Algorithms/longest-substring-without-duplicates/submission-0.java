class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0; 
        HashSet<String> subs = new HashSet<>(); 

        for(int i = 0; i < s.length(); i++){ 
          for(int j = i+1; j < s.length(); j++){ 
             if(subs.contains(s.substring(j,j+1))){ 
                break;
            }
            if(!subs.contains(s.substring(j,j+1))){ 
                subs.add(s.substring(j,j+1)); 
            }
            if(subs.size() > maxLength){ 
                maxLength = subs.size(); 
            }
          }
        }

        return maxLength; 
    }
}
