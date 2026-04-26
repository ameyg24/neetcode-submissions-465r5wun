class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        values = []
        for c in range(cols):
            if board[0][c] == "O":
                board[0][c] = "A"
                values.append((0,c))
            if board[rows-1][c] == "O":
                board[rows-1][c] = "A"
                values.append((rows-1,c))
        for r in range(1, rows-1):
            if board[r][0] == "O":
                board[r][0] = "A"
                values.append((r,0))
            if board[r][cols-1] == "O":
                board[r][cols-1] = "A"
                values.append((r,cols-1))
        def bfs(values):
            q = collections.deque(values)
            while q:
                r, c = q.popleft()
                directions = [(0,1),(0,-1),(1,0),(-1,0)]
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr in range(rows) and nc in range(cols):
                        if board[nr][nc] == "O":
                            board[nr][nc] = "A"
                            q.append((nr,nc))    
        bfs(values)        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "A":
                    board[r][c] = "O"
# board=
# [["O","X","X","O","X"],
# ["X","O","O","X","O"],
# ["X","O","X","O","X"],
# ["O","X","O","O","O"],
# ["X","X","O","X","O"]]