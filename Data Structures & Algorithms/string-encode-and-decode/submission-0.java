class Solution {
    List<String> stringArray = new ArrayList<>();  

    public String encode(List<String> strs) {
        String out = ""; 

        for(int i = 0; i < strs.size(); i++){
            out += strs.get(i); 
        }

        stringArray = strs;
        return out; 
    }

    

    public List<String> decode(String str) {
        return stringArray;
    }
}
