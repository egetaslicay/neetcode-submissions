class Solution {
    public int characterReplacement(String s, int k) {
    
    HashMap<Character, Integer> charCount = new HashMap<>(); 
    int maxWindow = 0; 

    int left = 0; 
    int maxFreq = 0; 
   

    for(int r = 0; r < s.length(); r++){ 
        charCount.put(s.charAt(r), charCount.getOrDefault(s.charAt(r), 0) + 1); 
        maxFreq = Math.max(maxFreq, charCount.get(s.charAt(r)));
        int windowLength = r - left +1; 
        while(windowLength - maxFreq > k){ 
            charCount.put(s.charAt(left), charCount.getOrDefault(s.charAt(left), 0) -1);
            left++;
            windowLength--;
        }

        maxWindow = Math.max(maxWindow, windowLength); 
    }

    return maxWindow;


    } 
}
