class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxstr = ""
        n = len(s)
        l = r = 0
        for i in range(n):
            l = r = i
            if i == 0:
                while l >= 0 and r <= n-1 and s[l] == s[r]:
                    maxstr = s[l:r + 1] if r-l+1 >= len(maxstr) else maxstr
                    r += 1
            elif i == n-1:
                while l >= 0 and r <= n-1 and s[l] == s[r]:
                    maxstr = s[l:r + 1] if r-l+1 >= len(maxstr) else maxstr
                    l -= 1
            else:
                while l >= 0 and r <= n-1 and s[l] == s[r]:
                    maxstr = s[l:r+1] if r-l+1 >= len(maxstr) else maxstr
                    l -= 1
                    r += 1
                l, r = i, i+1
                while l >= 0 and r <= n-1 and s[l] == s[r]:
                    maxstr = s[l:r+1] if r-l+1 >= len(maxstr) else maxstr
                    l -= 1
                    r += 1
        return maxstr     

