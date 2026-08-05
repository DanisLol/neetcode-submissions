class TimeMap:

    def __init__(self):
        self.t = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.t[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.t:
            return ""
        a = 0
        values = self.t[key]
        b = len(values) - 1
        result = ""
        while a <= b:
            mid = (a+b)//2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] > timestamp:
                
                b = mid-1
            else:
                result = values[mid][1]
                a = mid + 1
        return result
            

        


