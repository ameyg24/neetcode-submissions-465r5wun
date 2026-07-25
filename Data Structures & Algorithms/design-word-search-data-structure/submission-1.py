class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(word, curr):
            if len(word) == 0:
                return curr.end
            if word[0] == ".":
                for char in curr.children:
                    if dfs(word[1:], curr.children[char]):
                        return True
                return False
            if word[0] not in curr.children:
                return False
            curr = curr.children[word[0]]
            return dfs(word[1:], curr)
        return dfs(word, curr)

