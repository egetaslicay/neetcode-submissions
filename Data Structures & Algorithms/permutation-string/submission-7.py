from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Ctr = Counter(s1)
        s2Ctr = {}
        left = 0 
        right = len(s1)-1 

        for i in range(len(s1)): 
            if s2[i] not in s2Ctr: 
                s2Ctr[s2[i]] = 0 
            s2Ctr[s2[i]] += 1

        while(right < len(s2)): 
            if (s1Ctr == s2Ctr): 
                return True 

            s2Ctr[s2[left]] -= 1 
            s2Ctr[s2[right]] += 1 

        return false
    