import collections
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        # def bfs(r,c):
        #     q = collections.deque()
        #     q.append((r,c,0))
        #     # d = 2147483647
        #     while q:
        #         row, col, dist = q.popleft()
        #         print(row,col,dist)
        #         directions = [[1,0],[-1,0],[0,1],[0,-1]]
        #         for dr,dc in directions:
        #             r = dr+row
        #             c = col+dc
        #             newdist = dist + 1
        #             if ((r in range(rows)) and (c in range(cols))):
        #                 # if grid[r][c] == 2147483647:
        #                 #     grid[r][c] = dist
        #                 # if grid[r][c] > 0:
        #                 #     grid[r][c] = min(grid[r][c], dist)
        #                 if grid[r][c] > newdist:
        #                     grid[r][c] = newdist
        #                     q.append((r,c,newdist))
        #                 # if grid[r][c] > 0:
        #                 #     return dist + 1
        INF = 2147483647
        q = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        while q:
            row,col = q.popleft()
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in directions:
                r = row+dr
                c = col + dc
                if r in range(rows) and c in range(cols):
                    if grid[r][c] == INF:
                        grid[r][c] = grid[row][col] + 1
                        q.append((r,c))