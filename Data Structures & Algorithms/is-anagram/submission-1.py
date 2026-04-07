class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        if len(s) != len(t):
            return False
        for c in s:
            if c not in d1:
                d1[c] = 1
            else:
                d1[c] += 1
        for c in t:
            if c not in d1 or d1[c] == 0:
                return False
            d1[c] -= 1
        return True