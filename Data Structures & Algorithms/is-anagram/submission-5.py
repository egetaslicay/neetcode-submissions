class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        countert = Counter(t)
        counters = Counter(s)

        for char in countert: 
            if countert[char] != counters[char]: 
                return false

        return True