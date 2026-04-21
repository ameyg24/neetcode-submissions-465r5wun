class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = []
        intervals.sort()
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            print(intervals)
            print(res)
            if res[-1][0]<=intervals[i][0]<res[-1][1]:
                res[-1] = [res[-1][0], min(res[-1][1], intervals[i][1])]
            else:
                res.append(intervals[i])
        return len(intervals) - len(res)