from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        # scount = Counter(s)
        # tcount = Counter(t)
        n = len(t)
        # curr = 0
        scount = defaultdict(int)
        tcount = defaultdict(int)
        curr = 0
        for i in range(len(t)):
            tcount[t[i]]+=1
        # for i in range(n):
        #     if t[i] in scount and scount[t[i]] >= tcount[t[i]]:
        #         curr +=1
        print(scount)
        print(tcount)
        # print(curr, n)
        # if curr != n:
        #     return ""
        l= 0
        shortest = ""
        for r in range(len(s)):
            # if curr == n:
            #     return scount[l:r+1]   
            print(r,curr)      
            scount[s[r]] += 1
            print(scount)
            if s[r] in tcount and scount[s[r]]<=tcount[s[r]]:
                curr +=1
            while curr == n:
                if shortest == "":
                    shortest = s[l:r+1]
                elif r-l+1 < len(shortest):
                    shortest = s[l:r+1]
                if s[l] in tcount and scount[s[l]]-1<tcount[s[l]]:
                    break
                scount[s[l]]-=1
                l+=1 
            
        return shortest
                # if 
                # shortest = s[l:r+1] if r-l+1 >= len(shortest) else shortest
                # scount[s[l]]-=1
                # l+=1
                # scount[s[l]]+=1
                # if s[l] in tcount and scount[t[]]

        # while l<r and r-l+1 >= len(t):
        #     scount[s[l]]-=1
        #     lbool = False
        #     rbool = False
        #     if scount[s[l]] >= tcount[s[l]]:
        #         l+=1
        #     else:
        #         scount[s[l]]+=1 
        #         lbool = True
        #     scount[s[r]]-=1 
        #     if scount[s[r]] >= tcount[s[r]]:
        #         r-=1
        #     else:
        #         scount[s[r]]+=1 
        #         rbool = True
        #     if rbool and lbool:
        #         break 
        return s[l:r+1]                     
        # scount = {i:0 for i in range(52)}
        # tcount = {i:0 for i in range(52)}
        # print(ord("z"))
        # print(ord("a"))
        # print(ord("Z"))
        # print(ord("A"))      
        # print(ord("z")-ord("A"))
        # for i in range(len(t)):
        #     print(i)
        #     tidx = ord(t[i])-ord("a")
        #     print(tidx)
        #     tcount[tidx]+=1 
        #     sidx = ord(s[i])-ord("a")
        #     scount[sidx]+=1
        # correct = 0
        # for i in range(26):
        #     if tcount[i] > 0 and scount[i] == tcount[i]:
        #         correct +=1
        # print(correct)
        