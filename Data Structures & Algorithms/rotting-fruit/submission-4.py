from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        check = 0
        arr = []
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    check += 1
                if grid[r][c] == 2:
                    arr.append((r,c))
        def bfs(arr, check):
            q = deque(arr)
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            steps = 0
            while q and check > 0:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr in range(row) and nc in range(col) and grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            q.append((nr,nc))
                            check -= 1
                steps += 1
            return check, steps
        
        if check > 0:
            check, steps = bfs(arr, check)
        else:
            return 0
        return steps if check == 0 else -1