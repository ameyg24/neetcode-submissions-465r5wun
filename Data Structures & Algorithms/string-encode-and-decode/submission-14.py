class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for el in strs:
            n = len(el)
            res += str(n) + "#" + el
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i<len(s):
            j = i
            while s[j] != "#":
                j +=1
            count = int(s[i:j])
            i = j+1
            j = i + count
            res.append(s[i:j])
            i = j
        return res
