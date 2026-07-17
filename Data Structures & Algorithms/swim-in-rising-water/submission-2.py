import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        heap = [(grid[0][0], 0, 0)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while heap:
            val, r, c = heapq.heappop(heap)
            if r == c == n-1:
                return max(val, grid[n-1][n-1])
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if -1<nr <n and -1<nc<n and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    heapq.heappush(heap, (max(val, grid[nr][nc]), nr, nc))
