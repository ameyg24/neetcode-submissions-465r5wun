class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])
        outer = []
        for r in range(row):
            if board[r][0] == "O":
                outer.append((r,0))
                board[r][0] = "T"
            if board[r][col - 1] == "O":
                outer.append((r,col - 1))
                board[r][col-1] = "T"
        for c in range(1, col-1):
            if board[0][c] == "O":
                outer.append((0,c))
                board[0][c] = "T"
            if board[row-1][c] == "O":
                outer.append((row-1,c))
                board[row - 1][c] = "T"
        def dfs(arr):
            q = deque(arr)
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr in range(row) and nc in range(col) and board[nr][nc] == "O" :
                        board[nr][nc] = "T"
                        q.append((nr,nc))

        dfs(outer)
        print(board)
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"
        for r in range(row):
            for c in range(col):
                if board[r][c] == "T":
                    board[r][c] = "O"       

# board=    [["O","X","X","O","X"],
            # ["X","O","O","X","O"],
            # ["X","O","X","O","X"],
            # ["O","X","O","O","O"],
            # ["X","X","O","X","O"]]