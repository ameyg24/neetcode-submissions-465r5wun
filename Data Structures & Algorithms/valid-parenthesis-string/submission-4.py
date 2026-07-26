class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        leftmax = [0] * (n+1)
        leftmin = [0] * (n+1)
        for i in range(n):
            if s[i] == "(":
                leftmax[i+1] = leftmax[i] + 1
                leftmin[i+1] = leftmin[i] + 1
            elif s[i] == ")":
                leftmax[i+1] = leftmax[i] - 1
                leftmin[i+1] = leftmin[i] - 1  
            else:
                leftmax[i+1] = leftmax[i] + 1
                leftmin[i+1] = max(0, leftmin[i] - 1)
            if leftmax[i] < 0:
                return False
        print(leftmin, leftmax)
        return leftmin[-1] <=0 <= leftmax[-1]