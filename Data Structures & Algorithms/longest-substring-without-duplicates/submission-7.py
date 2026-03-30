class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0
        string = ""
        maxstr = ""
        while l<=r and r in range(len(s)):
            print(string)
            if s[r] not in string:
                string += s[r]
                r += 1
            else:
                if len(string) > len(maxstr):
                    maxstr = string
                while s[l] != s[r]:
                    l += 1
                l += 1
                string = s[l: r+ 1]
                r+= 1
            
        return max(len(string), len(maxstr))

