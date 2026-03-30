from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = []
        atlantic = []
        pi = []
        ai = []
        row, col = len(heights), len(heights[0])
        for c in range(col):
            pi.append((0,c))
            ai.append((row-1,c))
        for r in range(row):
            if r != 0:
                pi.append((r,0))
            if r != row - 1:
                ai.append((r,col-1))
        def bfs(arr):
            q = deque(arr)
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            visited = set(arr)
            while q:
                tr, tc = q.popleft()
                for dr,dc in directions:
                    nr, nc = tr + dr, tc + dc
                    if nr in range(row) and nc in range(col) and (nr,nc) not in visited and heights[nr][nc] >= heights[tr][tc]:
                        visited.add((nr,nc))
                        q.append((nr,nc))
            print(visited)
            return visited
        pacific = bfs(pi)
        atlantic = bfs(ai)
        res = []
        for (pr,pc) in pacific:
            if (pr, pc) in atlantic:
                res.append([pr,pc])
        return res           

