class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0 
        letterSet = set()
        left = 0
        right = 1 

        while(right < len(s) and left <= right): 
            
            while s[right] in letterSet: 
                letterSet.remove(s[left])
                l += 1  

            letterSet.add(s[right])
            right += 1
            res = max(res, len(letterSet))

        return res





