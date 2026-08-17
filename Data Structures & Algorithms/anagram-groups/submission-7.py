from collections import defaultdict
class Solution:
    def groupAnagramsDefaultDict(self, strs: List[str]) -> List[List[str]]:
        res = []  # List[List[str]]
        myDict = defaultdict(list)

        for word in strs: 
            count = [] 

            for char in word: 
                count[ord(char) - ord('a')] +=  1

            count = tuple(count)
            myDict[count].append(word)

        for key, value in myDict.items(): 
            res.append(value)
        
        return res