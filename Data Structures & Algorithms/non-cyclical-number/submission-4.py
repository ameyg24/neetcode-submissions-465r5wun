class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        sums = n
        while sums != 1:
            if sums in visited:
                return False
            else:
                visited.add(sums)
                num = str(sums)
                sums = 0
                for i in range(len(num)):
                    sums += (int(num[i]))**2
        return True