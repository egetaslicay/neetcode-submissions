class Solution {
    public int lengthOfLongestSubstring(String s) {
    int left = 0; 
    int maxLength = 0; 
    Set<Character> charSet = new HashSet<>(); 

    for(int r = 0; r < s.length(); r++){ 
        while(charSet.contains(s.charAt(r))){ 
            charSet.remove(s.charAt(left)); 
            left++;
        }

        charSet.add(s.charAt(r)); 
        maxLength = Math.max(r - left + 1, maxLength);
    }

    return maxLength; 
    }
}
