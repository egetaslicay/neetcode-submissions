class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tSet = set(t)
        tCounts = Counter(t)
        windowCount = defaultdict(int)

        left = 0 
        matches = 0 
        minWindowLength = float('inf')
        resIndices = []

        for right in range(len(s)): 

            windowCount[s[right]] += 1                       # grab the right string 
            if s[right] in tSet and windowCount[s[right]] == tCounts[s[right]]:   # update count and matches if needed 
                matches += 1 
            
            # while this window is valid matches == len(tSet): 
            while matches == len(tSet): 

                if (right - left + 1) < minWindowLength:  # record this as a possible result  record minWindowLength and the
                    minWindowLength = right - left + 1
                    resIndices = [left, right] 

                # pull left forwards, decrement the count of the letters and check beforehand if they
                if s[left] in tSet and windowCount[s[left]] == tCounts[s[left]]:
                    matches -= 1
                windowCount[s[left]] -= 1 
                left += 1   


        if not resIndices: 
            return "" 

        return s[resIndices[0]: resIndices[1]+1] 

        





