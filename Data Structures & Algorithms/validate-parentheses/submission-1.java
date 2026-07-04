class Solution {
    public boolean isValid(String s) {
    Stack<String> stack = new Stack<>();

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
            if(!stack.peek().equals(str) || stack.empty()){
                return false;
            } else { 
                stack.pop();
            }
        }
    }
    return true; 
    }
}
