class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW, COL = len(board), len(board[0])
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [[set() for _ in range(3)] for x in range(3)]
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] != ".":
                    if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxs[r//3][c//3]:
                        return False
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    boxs[r//3][c//3].add(board[r][c])
        print(rows)
        print(cols)
        print(boxs)
        return True
