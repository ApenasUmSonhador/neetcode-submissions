class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        curr = set()
        word = []
        for char in s:
            if char in curr:
                best = max(best, len(word))
                i = 0
                while word[i] != char:
                    curr.remove(word[i])
                    i+=1
                word = word[i+1:]
            else:
                curr.add(char)
            word.append(char)
        return max(best, len(word))
            