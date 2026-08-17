from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Map = Counter(s1)
        s2Map = Counter(s2[:len(s1)])

        matches = 0
        for key in s1Map:
            if s1Map[key] == s2Map[key]:
                matches += 1

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == len(s1Map):
                return True

            # add right char
            rc = s2[right]
            if s2Map[rc] == s1Map[rc]:
                matches -= 1
            s2Map[rc] += 1
            if s2Map[rc] == s1Map[rc]:
                matches += 1

            # remove left char
            lc = s2[left]
            if s2Map[lc] == s1Map[lc]:
                matches -= 1
            s2Map[lc] -= 1
            if s2Map[lc] == s1Map[lc]:
                matches += 1
            left += 1

        return matches == len(s1Map)