class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = collections.Counter(s1)
        l,r = 0, len(s1) - 1
        while r - l == len(s1) - 1 and r < len(s2):
            if count1[s2[l]] > 0 and count1[s2[r]] > 0:
                tmpl = l
                tmpr = r
                tmp = count1.copy()
                tmp[s2[r]]-=1
                print(l)
                while l < r:
                    if tmp[s2[l]] > 0:
                        tmp[s2[l]]-=1
                        l+=1
                    else:
                        break
                if l == r:
                    return True
                else:
                    l = tmpl + 1
                    r = tmpr + 1
            else:
                l+=1
                r+=1
        return False
                