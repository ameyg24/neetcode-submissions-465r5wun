class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])
        res = set()
        roo = Trie()
        for w in words:
            roo.add(w)
        visited = set()

        def dfs(r, c, curr, word):
            if r not in range(n) or c not in range(m) or (r,c) in visited or board[r][c] not in curr.children:
                return
            
            curr = curr.children[board[r][c]]
            visited.add((r,c))
            word += board[r][c]
            if curr.end:
                res.add(word)
            
            dfs(r+1,c, curr, word)
            dfs(r,c+1, curr, word)
            dfs(r-1,c, curr, word)
            dfs(r,c-1, curr, word)
            visited.remove((r,c))
        for r in range(n):
            for c in range(m):
                dfs(r,c,roo.root,"")
        return list(res)
        