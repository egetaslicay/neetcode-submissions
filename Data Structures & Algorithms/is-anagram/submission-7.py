class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounter = Counter(s)
        tCounter = Counter(t)

        for entry in sCounter: 
            if sCounter[entry] != tCounter[entry]: 
                return False

        return True 