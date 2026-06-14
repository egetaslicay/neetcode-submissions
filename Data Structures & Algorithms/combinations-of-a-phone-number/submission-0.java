class Solution {
    private List<String> result = new ArrayList<>(); 
    private String[] digitToChar = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public List<String> letterCombinations(String digits){ 
    if(digits.isEmpty()){ 
        return result;
    }

    backtrack(0, "", digits);
    return result;
    }

    private void backtrack(int index, String currString, String digits){ 
    if(currString.length() == digits.length()){ 
        result.add(currString);
        return; 
    }

    String chars = digitToChar[digits.charAt(index) - '0'];
    for(char c : chars.toCharArray()){
        backtrack(index+1, currString + c, digits); 
    }

    }
}