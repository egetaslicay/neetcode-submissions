class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        numReplacements = 0 
        left = 0 
        right = 0 
        myDict = defaultdict(int)
        maxFreq = 0 
        res = 0

        while left <= right and right < len(s):
            
            myDict[s[right]] += 1 
            maxFreq = max(maxFreq, myDict[s[right]])

            while ((right - left) + 1 - maxFreq > k): 
                myDict[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1) 
            right += 1 

        return res 
                


