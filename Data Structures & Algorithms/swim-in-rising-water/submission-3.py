import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0],0,0)]
        n = len(grid)
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        visited.add((0,0))
        while heap:
            height, row, col = heapq.heappop(heap)
            if row == n-1 and col == n-1:
                return height
            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                if nr in range(n) and nc in range(n) and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    heapq.heappush(heap, (max(height, grid[nr][nc]), nr, nc))

