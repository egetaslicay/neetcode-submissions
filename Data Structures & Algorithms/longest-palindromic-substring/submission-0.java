class Solution {
    public String longestPalindrome(String s) {
    int longest = 0; 
    String result = "";

    for(int i = 0; i < s.length(); i++){ 
        for(int j = i; j < s.length(); j++){
            int left = i;
            int right = j; 
            while(left < right && s.charAt(left) == s.charAt(right)){ 
                left++;
                right--;
            }

            if(left >= right && longest < (j-i + 1)){ 
                result = s.substring(i, j+1); 
                longest = j - i + 1;



            }



        }
    }

    return result;
    }
}

