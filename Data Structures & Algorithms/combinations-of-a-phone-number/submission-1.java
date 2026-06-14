class Solution {
    public List<String> letterCombinations(String digits){ 
    List<String> result = new ArrayList<>(); 
    if(digits.isEmpty()){
        return new ArrayList<>(); 
    }

    result.add(""); 
     String[] digitToChar = {
            "", "", "abc", "def", "ghi", "jkl",
            "mno", "qprs", "tuv", "wxyz"
        };

    for(char digit : digits.toCharArray()){ 
        List<String> temp = new ArrayList<>();
        for(String currString : result){ 
            for(char c : digitToChar[digit - '0'].toCharArray()){
                temp.add(currString +c);
            }
        }
        result = temp;
    }

    return result;

    }
}
