class Solution:
    def reverse(self, x: int) -> int:
        # sign = 1 if x >= 0 else -1
        # string = str(x)  
        # if sign == -1:
        #     string = string[1:]
        # revstr = string[::-1]
        # revnum = int(revstr)
        # if sign == -1:
        #     revnum *= -1
        # if not -2**31 <= revnum <= 2**31 - 1:
        #     return 0
        # return revnum

        def rev(n, tmp):
            if n == 0:
                return tmp
            tmp = tmp*10 + n%10
            return rev(n//10, tmp)
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = rev(x, 0)
        res *= sign
        print(res)
        if not -2**31 <= res <= 2**31 - 1:
            return 0
        return res