from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        INF = 2147483647
        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visited = [[False] * col for _ in range(row)]
            visited[r][c] = True
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            steps = 0
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    if grid[r][c] == 0:
                        return steps
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr in range(row) and nc in range(col) and not visited[nr][nc] and grid[nr][nc] != -1:
                            visited[nr][nc] = True
                            q.append((nr,nc))
                steps += 1
            return INF
        for r in range(row):
            for c in range(col):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r,c)
