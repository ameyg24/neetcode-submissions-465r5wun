import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(x**2+y**2, [x,y]) for x,y in points]
        heapq.heapify(distances)
        res = []
        while len(res) < k:
            dist, points = heapq.heappop(distances)
            res.append(points)
        return res