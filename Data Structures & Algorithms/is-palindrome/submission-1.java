class Solution {
    public boolean isPalindrome(String s) {
        if(s.length() == 1 || s == ""){ 
            return true;
        }

        s = s.toLowerCase(); 

        int left = 0; 
        int right = s.length() -1;

        while(left < right){ 
            char startChar = s.charAt(left); 
            char endChar = s.charAt(right); 

            if(!alphaNum(startChar)){ 
                left++;
            } else if(!alphaNum(endChar)){ 
                right--; 
            } else { 
            if(Character.toLowerCase(startChar) != Character.toLowerCase(endChar)){ 
                return false;
            }
            left++;
            right--; 
            }
        }
      return true;

    }


      public boolean alphaNum(char c) {
        return (c >= 'A' && c <= 'Z' ||
                c >= 'a' && c <= 'z' ||
                c >= '0' && c <= '9');
    }
}

