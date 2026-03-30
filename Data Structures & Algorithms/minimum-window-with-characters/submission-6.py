from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcount = defaultdict(int)
        scount = defaultdict(int)
        for char in t:
            tcount[char]+=1
        l = 0
        curr = ""
        shortest = ""
        count = 0
        for r in range(len(s)):
            if s[r] in tcount:
                scount[s[r]]+=1
                if scount[s[r]] <= tcount[s[r]]:
                    count +=1
            while count == len(t):
                shortest = s[l:r+1] if r-l+1 < len(shortest) or not shortest else shortest
                if s[l] in scount: scount[s[l]]-=1
                if s[l] in scount and scount[s[l]] < tcount[s[l]]:
                    count-=1
                l+=1
            print(l, r)
        return shortest