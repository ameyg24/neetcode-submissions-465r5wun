class Solution:
    def reverseBits(self, n: int) -> int:
        string = ""
        for i in range(32):
            if n & 1 == 1:
                string = string + "1"
            else:
                string = string + "0"
            n = n >> 1

        # string = str(n)
        # tmp = string[::-1]
        # print(string)
        # print(tmp)
        value = 0
        for i in range(32):
            value += (2 ** (31-i)) * int(string[i])
        return value