class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounter = Counter(s)
        tCounter = Counter(t)

        if len(sCounter) != len(tCounter): 
            return False 

        for entry in sCounter: 
            if sCounter[entry] != tCounter[entry]: 
                return False

        return True 