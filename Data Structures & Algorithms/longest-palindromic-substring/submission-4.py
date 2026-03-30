class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        maxlen = 0
        for i in range(n):
            # if n%2 != 0:
                l,r = i, i
                while l >= 0 and r < n and s[l] == s[r]:
                    if (r-l + 1) > maxlen:
                        res = s[l:r+1]
                        maxlen = r-l+1
                    l -= 1
                    r += 1
            # else:
                l, r = i, i + 1
                while l >= 0 and r < n and s[l] == s[r]:
                    if (r-l + 1) > maxlen:
                        res = s[l:r+1]
                        maxlen = r-l+1
                    l -= 1
                    r += 1
        return res