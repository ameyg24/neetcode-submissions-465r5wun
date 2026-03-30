class TreeMap:
    
    def __init__(self):
        self.treemap = {}

    def insert(self, key: int, val: int) -> None:
        self.treemap[key] = val

    def get(self, key: int) -> int:
        if key in self.treemap:
            return self.treemap[key]
        return -1

    def getMin(self) -> int:
        if not self.treemap:
            return -1
        mini = next(iter(self.treemap))
        for key in self.treemap:
            if key < mini:
                mini = key
        return self.treemap[mini]

    def getMax(self) -> int:
        if not self.treemap:
            return -1
        maxo = next(iter(self.treemap))
        for key in self.treemap:
            if key > maxo:
                maxo = key
        return self.treemap[maxo]

    def remove(self, key: int) -> None:
        if self.treemap:
            self.treemap.pop(key)
        
        

    def getInorderKeys(self) -> List[int]:
        lst = []
        for key in self.treemap:
            lst.append(key)
        lst.sort()
        return lst

