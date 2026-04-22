"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [x.start for x in intervals]
        starts.sort()
        ends = [x.end for x in intervals]
        ends.sort()
        si, ei = 0, 0
        maxroom = 0
        currval = 0
        while si < len(intervals):
            if starts[si] < ends[ei]:
                si += 1
                currval += 1
            else:
                ei += 1
                currval -= 1
            maxroom = max(maxroom, currval)
        return maxroom

