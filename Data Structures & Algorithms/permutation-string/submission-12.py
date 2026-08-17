from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Ctr = Counter(s1)
        s2Ctr = defaultdict(int)
        left = 0 
        right = len(s1)-1 


        if len(s1) > len(s2): 
            return False 
            
        for i in range(len(s1)): 
            s2Ctr[s2[i]] += 1

        while(right < len(s2)): 
            if (s1Ctr == s2Ctr): 
                return True 

            s2Ctr[s2[left]] -= 1 
            s2Ctr[s2[right]] += 1

            left += 1
            right += 1

        return False
    