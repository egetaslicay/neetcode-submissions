class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scounter = Counter(s)
        tcounter = Counter(t)
        return scounter == tcounter