class Solution {
    public boolean isValid(String s) {
    Stack<String> stack = new Stack<>();

    for(int i = 0; i < s.length(); i++){ 
        String str = s.substring(i, i+1); 
        if(str == "("){
            stack.push(")"); 
        }
        if(str == "{"){ 
            stack.push("}"); 
        }
        if(str == "[") { 
            stack.push("]");
        }

        if(str == ")" || str == "]" || str == "}"){ 
            if(stack.peek() != str){
                return false;
            } else { 
                stack.pop();
            }
        }
    }
    return true; 
    }
}
