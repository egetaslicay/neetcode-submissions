class Solution {
    public boolean isValid(String s) {
    if(s.length() == 0){
        return true; 
    }

    Map<Character, Character> bracketMap = new HashMap<>(); 
    bracketMap.put(')', '('); 
    bracketMap.put('}', '{'); 
    bracketMap.put(']','['); 

    Deque<Character> openingStack = new ArrayDeque<>();
    char[] charArray = s.toCharArray();


    for(int i = 0; i < charArray.length; i++){ 
        char curr = charArray[i]; 
        if(curr == ')' || curr == ']' || curr == '}'){ 
            if(openingStack.isEmpty()){ 
                return false;
            } else if(bracketMap.get(curr) != openingStack.peek()){
                return false;
            } else { 
                openingStack.pop();
            }
        } else { 
            openingStack.push(curr); 
        }
    }

    return openingStack.isEmpty();


    }
}
