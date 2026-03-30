class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        curr = collections.defaultdict(int)
        currstr = ""
        l = 0
        maxlen = 0
        maxf = 0
        for r in range(len(s)):
            print(currstr, maxlen)
            curr[s[r]] += 1
            currstr += s[r]
            maxf = max(maxf, curr[s[r]])
            while l<=r and len(currstr) - maxf > k:
                curr[s[l]] -= 1
                l+=1
                currstr = s[l:r+1]
            maxlen = max(maxlen, len(currstr))
        return maxlen
                