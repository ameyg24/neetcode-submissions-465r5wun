class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxcount = 0
        curr = defaultdict(int)
        l = 0
        for r in range(len(s)):
            curr[s[r]] += 1
            print(curr)
            if (r-l+1) - max(curr.values()) > k:
                while (r-l+1) - max(curr.values()) > k and l < r:
                    curr[s[l]]-=1
                    l += 1
            # if not (r-l+1) - max(curr.values()) > k: 
            maxcount = max(maxcount, r-l + 1)
            # maxcount = max(maxcount, r-l + 1) if (r-l+1) - max(curr.values()) > k else continue
            print(maxcount)
        return maxcount