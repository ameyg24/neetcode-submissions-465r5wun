from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        def bfs(x,y):
            q = deque()
            q.append((x,y))
            while q:
                curx, cury = q.popleft()
                directions = [(0,1),(0,-1),(1,0),(-1,0)]
                for dx, dy in directions:
                    tx, ty = curx + dx, cury + dy
                    if tx in range(rows) and ty in range(cols) and grid[tx][ty] == "1":
                        grid[tx][ty] = "-1"
                        q.append((tx,ty))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    res += 1
        return res