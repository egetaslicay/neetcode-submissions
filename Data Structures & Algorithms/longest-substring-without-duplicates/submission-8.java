class Solution {
    public int lengthOfLongestSubstring(String s) {
    if(s.length() == 0){
        return 0;
    }

    int left = 0; 
    int right = 0;
    int maxWindow = 0; 
    Set<Character> seenSet = new HashSet<>(); 

    while(right < s.length()){ 
        char curr = s.charAt(right);
        if(seenSet.contains(curr)){ 
            seenSet.remove(s.charAt(left)); 
            left++; 
        } else { 
            seenSet.add(curr); 
            maxWindow = Math.max(maxWindow, right - left + 1); 
            right++; 
            
        }
    }

    return maxWindow;


    }
}
