import collections
class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            tmp = 1
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    r = row +dr
                    c = col + dc
                    if ((r in range(rows)) and (c in range(cols)) and (grid[r][c] == 1) and ((r,c) not in visited)):
                        visited.add((r,c))
                        q.append((r,c))
                        tmp +=1 
            print(tmp)
            return tmp
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and ((r,c) not in visited):
                    x = bfs(r,c)
                    maxarea = max(maxarea, x)
        return maxarea