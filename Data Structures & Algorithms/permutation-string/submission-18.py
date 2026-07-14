from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0 
        right = len(s1)-1
        s1Map = Counter(s1)
        s2Map = Counter(s2[:len(s1)])


        # base case 
        if len(s1) > len(s2): 
            return False 


        while(right < len(s2)-1): 

            if(s1Map == s2Map):
                return True

            s2Map[s2[left]] -= 1
            if s2Map[s2[left]] == 0: 
                del s2Map[s2[left]]

            left += 1
            right += 1

            s2Map[s2[right]] += 1

        if s2Map == s1Map:
            return True

        
        return False