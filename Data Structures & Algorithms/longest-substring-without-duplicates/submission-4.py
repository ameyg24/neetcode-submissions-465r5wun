from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        tmp = ""
        maxlen = 0
        seen = set()
        while left <= right and left in range(len(s)) and right in range(len(s)):
            if s[right] in seen:
                print(tmp)
                maxlen = max(maxlen, len(tmp))
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                left += 1
            tmp = s[left:right + 1]
            seen.add(s[right])
            right += 1
        maxlen = max(maxlen, len(tmp))
        return maxlen