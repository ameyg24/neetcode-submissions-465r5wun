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
        i = 0
        while i < len(intervals):
            if starts[i].start < ends[ei].end:
                curr += 1
                i +=1
            else:
                ei += 1
                curr -=1
            res = max(res, curr)
        return res
