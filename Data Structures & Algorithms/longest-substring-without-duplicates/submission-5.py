class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        best = 0

        for right in range(len(s)):

            if s[right] in charSet:
                best = max(best, right - left)
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1

            charSet.add(s[right])
        return max(best, len(s) - left)