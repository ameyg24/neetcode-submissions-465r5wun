"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        maps = {}
        maps[node] = Node(node.val)
        q = deque()
        q.append(node)
        while q:
            curr = q.popleft()
            for nei in curr.neighbors:
                if nei not in maps:
                    maps[nei] = Node(nei.val)
                    q.append(nei)
                maps[curr].neighbors.append(maps[nei])
        return maps[node]


        