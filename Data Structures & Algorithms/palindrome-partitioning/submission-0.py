class Solution:
    def partition(self, s: str) -> List[List[str]]:
        currstr = ""
        currstack = []
        res = []
        def ispali(string):
            l, r = 0, len(string) - 1
            while l <= r:
                if string[r] == string[l]:
                    r-=1
                    l+=1
                else:
                    return False
            return True
        def dfs(i, currstr):
            if i == len(s):
                currlen = 0
                for char in currstack:
                    currlen += len(char)
                if currlen == len(s): res.append(currstack.copy())
                return
            currstr += s[i]
            if ispali(currstr):
                currstack.append(currstr)
                dfs(i+1, "")
                currstack.pop()
            # while i + 1 in range(len(s)) and s[i] == s[i+1]:
            #     i+=1
            dfs(i+1, currstr)
        dfs(0, "")
        return res