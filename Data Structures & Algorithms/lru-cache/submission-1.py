class Node:
    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.maps = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next = self.right
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.maps:
            self.remove(self.maps[key])
            self.insert(self.maps[key])
            return self.maps[key].val
        else:
            return -1
    
    def put(self, key: int, value: int) -> None:
        tmp = Node(key, value)
        if key in self.maps:
            self.remove(self.maps[key])
        self.maps[key] = tmp
        self.insert(tmp)
        if len(self.maps) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.maps[lru.key]


