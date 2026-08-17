from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        right = 0 
        res = 0 
        maxF = 0 
        hashMap = defaultdict(int)

        while(right < len(s) and left <= right): 
            hashMap[s[right]] += 1
            maxF = max(maxF, hashMap[s[right]]) 

            while (k < (right - left) + 1 - maxF): 
                hashMap[s[left]] -= 1 

            res = max(right-left + 1, res)
            right += 1 

        return res