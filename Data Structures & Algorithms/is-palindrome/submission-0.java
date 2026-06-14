class Solution {
    public boolean isPalindrome(String s) {
        
        s = s.toLowerCase();
        s = s.replaceAll("\\s+", ""); 
        s = s.replaceAll("[^a-z0-9]", ""); 

        for(int i = s.length(); i > 0; i--){
            if(!s.substring(i-1, i).equals(s.substring(s.length() - i, s.length() - i + 1))){
                return false; 
            }
        }
        return true; 
        
    }
}
