class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        for i in range(len(temperatures)):
            tmp = 1
            for j in range(i + 1, len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    break
                tmp += 1
            ans.append(tmp if tmp != len(temperatures)-(i) else 0)
        return ans
        