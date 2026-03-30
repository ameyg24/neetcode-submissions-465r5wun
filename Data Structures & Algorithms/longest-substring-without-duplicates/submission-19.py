class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxstr = ""
        curr = ""
        seen = set()
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                curr += s[r]
                maxstr = curr if len(curr)>len(maxstr) else maxstr
            else:
                while s[l] != s[r] and l <= r:
                    seen.remove(s[l])
                    l+=1
                l+=1
                curr = s[l:r+1]
        return len(maxstr)