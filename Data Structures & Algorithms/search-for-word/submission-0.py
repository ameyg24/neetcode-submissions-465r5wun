class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        tmp = ""
        row, col = len(board), len(board[0])
        string = ""
        def dfs(r, c, i, visited):
            if r not in range(row) or c not in range(col) or (r,c) in visited or board[r][c] != word[i]:
                return False
            if i + 1 == len(word):
                return True
            visited.add((r,c))
            if dfs(r+1,c, i+1, visited) or dfs(r,c+1,i+1, visited) or dfs(r-1,c,i+1,visited) or dfs(r,c-1,i+1,visited):
                return True
            visited.remove((r,c))
            return False
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    visited = set()
                    if dfs(r,c,0, visited):
                        return True
        return False
        