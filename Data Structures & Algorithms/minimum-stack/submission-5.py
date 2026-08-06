class MinStack:

    items: list

    def __init__(self):
        self.items = []
        self.temp = []

    def push(self, val: int) -> None:
        self.items.append(val)
        if self.temp != []:
            self.temp.append(min(val, self.temp[-1]))
        else:
            self.temp.append(val)

    def pop(self) -> None:
        self.items.pop()
        self.temp.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.temp[-1]



        
