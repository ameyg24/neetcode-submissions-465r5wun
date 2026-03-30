import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            dist = -(x**2+y**2)
            heap.append((dist, (x,y)))
        heapq.heapify(heap)
        while len(heap) != k:
            heapq.heappop(heap)
        ans = []
        for h in heap:
            ans.append(h[1])
        return ans