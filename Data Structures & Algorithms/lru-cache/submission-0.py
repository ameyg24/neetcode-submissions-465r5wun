class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.HashMap = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.HashMap:
            self.HashMap.move_to_end(key)
            return self.HashMap[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.HashMap:
            self.HashMap[key] = value
            self.HashMap.move_to_end(key)
        else:
            self.HashMap[key] = value
            self.HashMap.move_to_end(key)
        if len(self.HashMap) > self.capacity:
            self.HashMap.popitem(last=False)
