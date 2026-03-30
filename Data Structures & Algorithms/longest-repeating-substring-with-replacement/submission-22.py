class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        curr = collections.defaultdict(int)
        l = 0
        maxlen = 0
        maxf = 0
        for r in range(len(s)):
            curr[s[r]] += 1
            maxf = max(maxf, curr[s[r]])
            while l<=r and r-l+1 - maxf > k:
                curr[s[l]] -= 1
                l+=1
            maxlen = max(maxlen, r-l+1)
        return maxlen
                