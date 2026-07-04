class Solution {
    public boolean isValid(String s) {
    Stack<Character> stack = new Stack<>(); 
    Map<Character, Character> bracketMap = new HashMap<>(); 

    bracketMap.put('(', ')'); 
    bracketMap.put('[', ']'); 
    bracketMap.put('{', '}'); 


    for(int i = 0; i < s.length(); i++){ 
        char currChar = s.charAt(i); 

        // opening bracket case 
        if(bracketMap.containsKey(currChar)){ 
            stack.push(bracketMap.get(currChar)); 
        } else { 
            if(stack.peek() == currChar){ 
                stack.pop();
            } else { 
                return false;
            }
        } 

    }


    return stack.isEmpty();

    }
}
