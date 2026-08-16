class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if not strs:
            return res
        min_len = float("inf")
        for s in strs:
            min_len = min(min_len, len(s))
        print(min_len)
        for i in range(min_len):
            t = strs[0][i]
            for s in strs:
                if s[i] != t:
                    return res
            res += t
        return res