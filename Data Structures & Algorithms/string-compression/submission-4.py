class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        l, r = 0, 0
        while l <= r and r < len(chars):
            if chars[l] == chars[r]:
                r += 1
            else:
                s += chars[l]
                if r-l > 1:
                    s += str(r-l)
                l = r
        s += chars[l]
        if r-l > 1:
            s += str(r-l)
        print(s)
        for i in range(len(s)):
            if i < len(chars):
                chars[i] = s[i]
        return len(s)