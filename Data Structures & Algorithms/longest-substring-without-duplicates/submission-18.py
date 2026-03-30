class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0
        maxstr = ""
        curr = ""
        seen = set()
        while l <= r and r in range(len(s)):
            print(curr)
            print(seen)
            if s[r] not in seen:
                curr += s[r]
                seen.add(s[r])
                r += 1
                maxstr = curr if len(curr) > len(maxstr) else maxstr
            else:
                while s[l] != s[r] and l <=r:
                    seen.remove(s[l])
                    l+=1
                l+=1
                r+=1
                curr = s[l:r]
        return len(maxstr)
# pwwkew
# pw
# 
