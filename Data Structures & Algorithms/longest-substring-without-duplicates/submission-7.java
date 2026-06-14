class Solution {
    public int lengthOfLongestSubstring(String s) {
    if(s.length() == 0){ 
        return 0; 
    }

    int left = 0; 
    int right = 0;     
    int maxWin = 0; 
    

    Set<Character> seenChars = new HashSet<>();

    while(right < s.length()) { 
        char currChar = s.charAt(right); 
        if(seenChars.contains(currChar)) { 
            seenChars.remove(s.charAt(left)); 
            left++; 
        } else { 
            seenChars.add(currChar); 
            int currWin = right - left + 1; 
            maxWin = Math.max(maxWin, currWin); 
            right++; 
        }
    }

    return maxWin;

    }
}
