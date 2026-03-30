from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        count = 0
        def bfs(r, c):
            queue = deque()
            queue.append((r,c))
            grid[r][c] = -1
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(row) and nc in range(col) and grid[nr][nc] == "1":
                        queue.append((nr, nc))
                        grid[nr][nc] = "-1"
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    bfs(r,c)
                    count += 1
        return count