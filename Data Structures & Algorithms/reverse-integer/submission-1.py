class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        string = str(x)  
        if sign == -1:
            string = string[1:]
        revstr = string[::-1]
        revnum = int(revstr)
        if sign == -1:
            revnum *= -1
        if not -2**31 <= revnum <= 2**31 - 1:
            return 0
        return revnum