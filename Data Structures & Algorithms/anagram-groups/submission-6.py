class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for x in strs:
            alpha_array = [0]*26
            for c in x:
                alpha_array[ord(c) - 97] += 1
            res[tuple(alpha_array)].append(x)
        return list(res.values())
        