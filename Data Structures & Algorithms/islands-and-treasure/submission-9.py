class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        def bfs(values):
            q = collections.deque()
            for val in values:
                q.append(val)
            while q:
                r, c, dist = q.popleft()
                directions = [(0,1),(0,-1),(1,0),(-1,0)]
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = dist + 1
                        q.append((nr,nc,dist+1))
        zeros = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    zeros.append((r,c,0))
        bfs(zeros)

                