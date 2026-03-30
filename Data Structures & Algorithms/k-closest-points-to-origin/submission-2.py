import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            dist = (x**2+y**2)
            heap.append((dist, (x,y)))
        heapq.heapify(heap)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        # for h in heap:
        #     ans.append(h[1])
        return ans