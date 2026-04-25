"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graph = {}
        if not node or not node.val:
            return None
        def dfs(node):
            if node not in graph:
                graph[node] = Node(node.val)
            for el in node.neighbors:
                if el not in graph:
                    graph[el] = Node(el.val)
                    dfs(el)
                graph[node].neighbors.append(graph[el])
        dfs(node)
        return graph[node]
        