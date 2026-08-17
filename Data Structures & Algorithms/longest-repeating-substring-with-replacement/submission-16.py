class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return len(s)
        charCount = defaultdict(int)
        left = 0
        right = 1
        maxLength = 0
        while right < len(s):
            charCount[s[right]] += 1
            for char, count in charCount.items():
                length = right-left
                if length - count > k:
                    maxLength = max(maxLength, length)
                    while s[left] == char:
                        charCount[s[left]] -= 1
                        left += 1
            right += 1

        return max(maxLength, right-left)