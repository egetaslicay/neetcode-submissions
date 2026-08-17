class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        haveMap = Counter(t)
        needMap = Counter(t)

        have = 0 
        need = len(needMap) 

        right = 0 
        left = 0 

        res = s

        if len(t) > len(s): 
            return ""

        # at the start we have nothing so we want to fill it with zero 
        for key in haveMap: 
            haveMap[key] = 0

        while(left <= right and right < len(s)): 
            
            if s[right] in haveMap: 
                haveMap[s[right]] += 1

                if haveMap[s[right]] == needMap[s[right]]: 
                    have += 1
                     

            while(have == need): 
                if len(s[left:right+1]) < len(res): 
                    res = s[left:right+1]

                if s[left] in haveMap: 
                    if haveMap[s[left]] == needMap[s[left]]: 
                        have -= 1
                    haveMap[s[left]] -= 1 
                
                left += 1 

            right += 1

    

        return res 
            





