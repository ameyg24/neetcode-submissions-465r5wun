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
        clones = {}
        if not node:
            return node
        clones[node] = Node(node.val)
        q = deque()
        q.append(node)
        while q:
            n = q.popleft()
            for nei in n.neighbors:
                if nei not in clones:
                    clones[nei] = Node(nei.val)
                    q.append(nei)
                clones[n].neighbors.append(clones[nei])
        return clones[node]