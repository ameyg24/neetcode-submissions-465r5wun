class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = []
        for i in range(len(digits)-1,-1,-1):
            tmp = digits[i] + carry
            if tmp > 9:
                carry = 1
                res = [0] + res
            else:
                carry = 0
                res = [tmp] + res
        if carry == 1:
            res = [1] + res
        return res
            