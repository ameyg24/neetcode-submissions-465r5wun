class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def row(board):
            for i in range(9):
                arr = ["1","2","3","4","5","6","7","8","9"]
                for j in range(9):
                    if board[i][j] in arr:
                        arr.remove(board[i][j])
                    elif board[i][j] == ".":
                        continue
                    else:
                        return False
            return True
        def column(board):
            for i in range(9):
                arr = ["1","2","3","4","5","6","7","8","9"]
                for j in range(9):
                    if board[j][i] in arr:
                        arr.remove(board[j][i])
                    elif board[j][i] == ".":
                        continue
                    else:
                        return False
            return True
        def three(board):
            for k in range(3):
                arr = ["1","2","3","4","5","6","7","8","9"]
                for i in range(3*k, 3*(k+1)):
                    for j in range(0, 3):
                        if board[i][j] in arr:
                            arr.remove(board[i][j])
                        elif board[i][j] == ".":
                            continue
                        else:
                            return False
            for k in range(3):
                arr = ["1","2","3","4","5","6","7","8","9"]
                for i in range(3*k, 3*(k+1)):
                    for j in range(3, 6):
                        if board[i][j] in arr:
                            arr.remove(board[i][j])
                        elif board[i][j] == ".":
                            continue
                        else:
                            return False
            for k in range(3):
                arr = ["1","2","3","4","5","6","7","8","9"]
                for i in range(3*k, 3*(k+1)):
                    for j in range(6, 9):
                        if board[i][j] in arr:
                            arr.remove(board[i][j])
                        elif board[i][j] == ".":
                            continue
                        else:
                            return False
            return True
        return column(board) and row(board) and three(board)
