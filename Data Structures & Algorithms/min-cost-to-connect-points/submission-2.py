import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(0, points[0][0], points[0][1])]
        n = len(points)
        visited = set()
        cost = 0
        while len(visited) < n:
            dist, x, y = heapq.heappop(heap)
            if (x,y) not in visited:
                visited.add((x,y))
                cost += dist
                for nx, ny in points:
                    if (nx, ny) not in visited:
                        heapq.heappush(heap, (abs(nx-x) + abs(ny-y), nx, ny))
        return cost