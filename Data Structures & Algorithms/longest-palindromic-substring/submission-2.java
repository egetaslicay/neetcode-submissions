class Solution {
    public String longestPalindrome(String s){ 
        int maxLength = 0; 
        String result = ""; 

        for(int i = 0; i < s.length(); i++){ 
            
            // odd length 
            int left = i; 
            int right = i; 
            while(left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)){ 
                if(right - left + 1 > maxLength){ 
                    maxLength = right - left +1; 
                    result = s.substring(left, right+1);
                }
                left--; 
                right++; 
            }

            // even length 
            left = i; 
            right = i+1; 
            while(left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)){ 
                if(right - left + 1 > maxLength){ 
                    result = s.substring(left, right+1);
                    maxLength = right - left + 1;
                }
                left--;
                right++;
            }

  


        }



              return result;
    }

}

