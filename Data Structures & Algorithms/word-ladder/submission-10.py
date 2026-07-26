from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjlist = defaultdict(list)
        def close(word1, word2):
            if len(word1) != len(word2):
                return False
            diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1
            return diff == 1
        for word in wordList:
            if close(beginWord, word):
                adjlist[beginWord].append(word)
                adjlist[word].append(beginWord)
        for i in range(len(wordList)):
            for j in range(len(wordList)):
                if i != j and close(wordList[i], wordList[j]):
                    adjlist[wordList[i]].append(wordList[j])
                    adjlist[wordList[j]].append(wordList[i])
        q = deque()
        q.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)
        res = 0
        while q:
            word, length = q.popleft()
            if word == endWord:
                res = length
                return res
            for adj in adjlist[word]:
                if adj not in visited:
                    visited.add(adj)
                    q.append((adj, length + 1))
        return res
            
        
