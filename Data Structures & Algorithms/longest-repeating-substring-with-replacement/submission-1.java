class Solution {
    public int characterReplacement(String s, int k) {
    int left = 0; 
    int maxWindow = 0; 
    int maxFreq = 0; 

    Map<Character, Integer> charCount = new HashMap<>();

    for(int r = 0; r < s.length(); r++){ 
    
    char curr = s.charAt(r);   
    charCount.put(curr, charCount.getOrDefault(curr, 0)+1);
    maxFreq = Math.max(maxFreq, charCount.get(curr)); 
    int windowLength = r - left + 1;
   
    while(windowLength - maxFreq > k){ 
        char leftChar = s.charAt(left);
        charCount.put(leftChar , charCount.get(leftChar) -1); 
        left++;
        windowLength--; 
    }

    maxWindow = Math.max(windowLength, maxWindow); 

    }
        
    return maxWindow; 
    } 
}
