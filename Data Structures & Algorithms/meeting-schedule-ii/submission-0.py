"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        starts = sorted(intervals, key = lambda x: x.start)
        ends = sorted(intervals, key = lambda x: x.end)
        curr = 0
        res = 0
        ei = 0
        for i in range(len(intervals)):
            if starts[i].start < ends[ei].end:
                curr += 1
            else:
                res = max(res, curr)
                ei += 1
        return max(res, curr)
