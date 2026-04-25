class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited = set()
            visited.add((r,c))
            curr = 1
            while q:
                r, c = q.popleft()
                directions = [(0,1),(0,-1),(1,0),(-1,0)]
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        curr += 1
                        q.append((nr,nc))
            return curr
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, bfs(r,c))
        return res