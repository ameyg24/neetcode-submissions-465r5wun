from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROW, COL = len(grid), len(grid[0])
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            while q:
                r,c = q.popleft()
                directions = [(0,1),(0,-1),(1,0),(-1,0)]
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if nr in range(ROW) and nc in range(COL) and grid[nr][nc] == "1":
                        q.append((nr,nc))
                        grid[nr][nc] = "-1"

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    count +=1
                    bfs(r,c)
        return count