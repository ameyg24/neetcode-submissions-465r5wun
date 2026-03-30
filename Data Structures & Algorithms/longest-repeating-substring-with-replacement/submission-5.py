from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maps = defaultdict(int)
        maxs = 0
        for r in range(len(s)):
            maps[s[r]] += 1
            if (r-l+1) - max(maps.values()) > k:
                maps[s[l]] -= 1
                l += 1
            maxs = max(maxs, r-l+1)
        return maxs