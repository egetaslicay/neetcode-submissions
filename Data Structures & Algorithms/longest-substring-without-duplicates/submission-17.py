class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0 
        right = left 
        chars = set()

        while left <= right and right < len(s):

            while s[right] in chars: 
                chars.remove(s[left])
                left += 1 

            chars.add(s[right])
            right += 1 
            
            res = max(res, right - left)

        return res 







