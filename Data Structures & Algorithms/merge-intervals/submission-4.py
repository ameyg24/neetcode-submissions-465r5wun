class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            x, y = intervals[i]
            if res[-1][0] <= x <= res[-1][1]:
                res[-1] = [res[-1][0], max(y, res[-1][1])]
            else:
                res.append([x,y])
        return res