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
        h = head
        if not h:
            return None
        curr = Node(head.val)
        maps[head] = curr
        while h.next:
            h = h.next
            tmp = Node(h.val)
            curr.next = tmp
            maps[h] = tmp
            curr = curr.next

        res = tmp = maps[head]

        while tmp != None and head != None:
            if head.random:
                x = maps[head.random]
                tmp.random = x
            tmp = tmp.next
            head = head.next
        return res
            



