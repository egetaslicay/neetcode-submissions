class Solution {
    public boolean isValid(String s) {
    Stack<String> stack = new Stack<>();
    closed = false; 

    for(int i = 0; i < s.length(); i++){ 
        String str = s.substring(i, i+1); 
        if(str.equals("(")){
            stack.push(")"); 
        }
        if(str.equals("{")){ 
            stack.push("}"); 
        }
        if(str.equals("[")) { 
            stack.push("]");
        }

        if(str.equals(")") || str.equals("}")  || str.equals("]")){ 
            if(stack.empty() || !stack.peek().equals(str)){
                return false;
            } else { 
                stack.pop();
            }
        }
    }
    return stack.empty(); 
    }
}
