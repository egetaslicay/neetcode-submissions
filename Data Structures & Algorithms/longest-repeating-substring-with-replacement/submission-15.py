from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        right = 0 
        hashMap = defaultdict(int) 
        maxFreq = 0 
        res = 0

        while(right < len(s) and left <= right): 
            hashMap[s[right]] += 1
            maxFreq = max(maxFreq, hashMap[s[right]])
                
            while(right - left + 1 - maxFreq > k): 
                hashMap[s[left]] -= 1 
                left += 1
            res = max(res, right-left + 1)
            right += 1 
        return res