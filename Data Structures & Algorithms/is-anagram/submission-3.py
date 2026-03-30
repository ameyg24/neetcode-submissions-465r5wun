class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap = collections.defaultdict(int)
        tmap = collections.defaultdict(int)
        for schar, tchar in zip(s,t):
            smap[schar] +=1
            tmap[tchar]+=1
        return smap == tmap