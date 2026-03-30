class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        diff = 0
        L = 0
        tmp = set()
        for R in range(n):
            while (s[R] in tmp):
                tmp.remove(s[L])
                L +=1
            tmp.add(s[R])
            diff = max(diff, R-L+1)
        return diff
        