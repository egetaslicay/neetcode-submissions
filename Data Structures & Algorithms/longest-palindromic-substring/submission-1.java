class Solution {
    public String longestPalindrome(String s) {
    String res = ""; 
    int resLength = 0; 

    for(int i = 0; i < s.length(); i++){ 
        for(int j = i; j < s.length(); j++){ 
            int left = i; 
            int right = j; 
            
            while(left < right && s.charAt(left) == s.charAt(right)){ 
                left++;
                right--;
            }

            if(left >= right && resLength < (j - i +1)){ 
                resLength = j-i + 1; 
                res = s.substring(i, j+1); 
            }





        }

    }

    return res;



        }
}
