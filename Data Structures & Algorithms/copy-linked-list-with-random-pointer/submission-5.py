"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        maps = {}
        curr = head
        while curr:
            tmp = Node(curr.val)
            maps[curr] = tmp
            curr = curr.next
        t = head
        maps[None] = None
        while t:
            val = maps[t]
            val.next = maps[t.next]
            val.random = maps[t.random]
            t = t.next
        return maps[head]