class TimeMap:

    def __init__(self):
        self.maps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.maps:
            self.maps[key] = [[value, timestamp]]
        else:
            self.maps[key].append([value, timestamp])
    
                

    def get(self, key: str, timestamp: int) -> str:
        print(self.maps)
        if key not in self.maps:
            return ""
        else:
            if self.maps[key][-1][1] <= timestamp:
                return self.maps[key][-1][0]
            l, r = 0, len(self.maps[key]) - 1
            while l <= r:
                mid = (l+r)//2
                if timestamp > self.maps[key][mid][1]:
                    l = mid + 1
                elif timestamp < self.maps[key][mid][1]:
                    r = mid - 1
                else:
                    return self.maps[key][mid][0]
            return self.maps[key][r][0] if r >= 0 else ""
