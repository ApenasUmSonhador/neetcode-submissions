class TimeMap:

    def __init__(self):
        self.times = {}
        self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.times:
            self.times[key].append(timestamp)
            self.values[key].append(value)
        else:
            self.times[key] = [timestamp]
            self.values[key] = [value]

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.times:
            return ""
        l = 0
        r = len(self.times[key]) - 1
        index = -1
        while l <= r:
            m = (l+r)//2
            print(m, index, l, r)
            if self.times[key][m] == timestamp:
                index = m
                break
            if self.times[key][m] <= timestamp:
                l = m+1
                index = m
            else:
                r = m-1
        if index == -1:
            return ""
        return self.values[key][index]