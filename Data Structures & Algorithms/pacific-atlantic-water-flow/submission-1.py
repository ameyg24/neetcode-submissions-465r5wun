class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = []
        atlantic = []
        for c in range(cols):
            pacific.append((0,c))
            atlantic.append((rows-1,c))
        for r in range(1, rows):
            pacific.append((r,0))
        for r in range(rows-1):
            atlantic.append((r,cols - 1))
        def bfs(values):
            q = collections.deque()
            visited = set()
            for val in values:
                q.append(val)
                visited.add(val)
            while q:
                r, c = q.popleft()
                directions = [(0,1),(0,-1),(1,0),(-1,0)]
                for dr, dc in directions:
                    nr, nc = r+dr, c + dc
                    if nr in range(rows) and nc in range(cols) and heights[nr][nc]>=heights[r][c] and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))
            return visited
        pacs = bfs(pacific)
        atl = bfs(atlantic)
        return [(r,c) for (r,c) in pacs if (r,c) in atl]
