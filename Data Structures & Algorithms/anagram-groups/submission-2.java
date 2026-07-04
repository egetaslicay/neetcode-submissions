class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if(strs.length == 0 || strs == null){
            return null; 
        }


        Set<String> addedStrings = new HashSet<>(); 
        List<List<String>> resultList = new ArrayList<>(); 

        for(int i = 0; i < strs.length; i++){ 
        List<String> innerResult = new ArrayList<>(); 
        String currWord = strs[i]; 
        innerResult.add(currWord); 

        if(addedStrings.contains(currWord)) { 
            continue; 
        }    

        for(int j = i+1; j < strs.length; j++){ 
        String compWord = strs[j]; 
        
        if(addedStrings.contains(currWord)) { 
            continue; 
        }    

        if(isAnagram(currWord, compWord)){ 
            innerResult.add(compWord);
            addedStrings.add(compWord);
        }

        }

        resultList.add(innerResult); 
    }


    return resultList;

    }

    public boolean isAnagram(String s, String t){ 
    if(s.length() != t.length()){
        return false;
    }

    Map<Character, Integer> sMap = new HashMap<>(); 
    Map<Character, Integer> tMap = new HashMap<>(); 

    for(int i = 0; i < s.length(); i++){ 
    char sChar = s.charAt(i); 
    char tChar = t.charAt(i); 

    sMap.put(sChar, sMap.getOrDefault(sChar, 0)+1);
    tMap.put(tChar, tMap.getOrDefault(tChar, 0)+1); 
    }

    return sMap.equals(tMap); 
    }
}