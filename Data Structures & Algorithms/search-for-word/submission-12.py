class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        n = len(word) - 1
        curr = ""
        visited = set()
        def dfs(r, c, i):
            nonlocal curr
            if r not in range(row) or c not in range(col) or board[r][c] != word[i] or (r,c) in visited:
                return False
            if i == n:
                return True
            curr += board[r][c]
            visited.add((r,c))
            ans = dfs(r+1,c,i+1) or dfs(r,c+1,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1)
            visited.remove((r,c))
            return ans
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        return False