class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return False
        ROW, COL = len(board), len(board[0])
        n = len(word)
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(r,c,i):
            if r in range(ROW) and c in range(COL) and board[r][c] == word[i] and (r,c) not in visited:
                visited.add((r,c))
                print(visited)
                if i == n-1:
                    return True
                else:
                    tmp = dfs(r+1,c,i+1) or dfs(r, c+1, i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1)
                    visited.remove((r,c))
                    return tmp
            else:
                return False



        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == word[0]:
                    visited = set()
                    if dfs(r,c,0):
                        return True
        return False



# board=[["A","B","C","E"],
        # ["S","F","E","S"],
        # ["A","D","E","E"]]
# word="ABCESEEEFS"