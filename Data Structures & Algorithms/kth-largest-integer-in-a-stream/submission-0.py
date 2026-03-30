class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.array = nums
        self.k = k

    def add(self, val: int) -> int:
        self.array.append(val)
        sort = self.array.sort()
        return self.array[-self.k]
        
