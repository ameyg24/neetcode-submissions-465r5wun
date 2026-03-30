from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        check = 0
        def bfs(arr):
            q = deque(arr)
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            steps = 0
            count = 0
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr in range(row) and nc in range(col) and grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            q.append((nr,nc))
                            count += 1
                steps += 1
            return count, steps - 1
        tmp = 0
        arr = []
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    check += 1
                if grid[r][c] == 2:
                    arr.append((r,c))
        if check > 0:
            count, steps = bfs(arr)
        else:
            return 0
        return steps if count == check else -1