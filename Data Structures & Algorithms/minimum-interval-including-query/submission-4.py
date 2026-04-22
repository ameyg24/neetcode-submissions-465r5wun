import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        minheap = []
        i = 0
        res = {}
        tmp = queries.copy()
        queries.sort()
        intervals.sort()
        print(queries)
        print(intervals)
        for el in queries:
            while i < len(intervals) and el >= intervals[i][0]:
                if el <= intervals[i][1]:
                    heapq.heappush(minheap, (intervals[i][1]-intervals[i][0]+1, intervals[i][1]))
                i += 1
            while minheap and minheap[0][1] < el:
                heapq.heappop(minheap)
            print(minheap)
            if minheap:
                res[el] = minheap[0][0]
            else:
                res[el] = -1
        print(tmp)
        return [res[el] for el in tmp]
            
            