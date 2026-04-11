class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for w in strs:
            ans += (chr(len(w)) + w)
        return ans

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i < len(s):
            n = ord(s[i])
            i += 1+n
            ans.append(s[i-n:i])
        return ans