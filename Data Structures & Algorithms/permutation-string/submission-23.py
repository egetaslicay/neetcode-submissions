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
            if rc in s1Map:
                s1_count = s1Map[rc]
                if s2Map[rc] == s1_count:
                    matches -= 1
                s2Map[rc] += 1
                if s2Map[rc] == s1_count:
                    matches += 1
            else:
                s2Map[rc] += 1

            # remove left char
            lc = s2[left]
            if lc in s1Map:
                s1_count_lc = s1Map[lc]
                if s2Map[lc] == s1_count_lc:
                    matches -= 1
                s2Map[lc] -= 1
                if s2Map[lc] == s1_count_lc:
                    matches += 1
            else:
                s2Map[lc] -= 1
            left += 1

        return matches == len(s1Map)