class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for w in strs:
            ans += (str(len(w)) + "-" + w)
        return ans

    def decode(self, s: str) -> List[str]:
        i=0
        ans = []
        while i < len(s):
            n = ""
            
            while s[i] != "-":
                n += s[i]
                i += 1
            
            n = int(n)
            w = s[i+1:i+n+1]
            ans.append(w)
            i += n+1
        return ans