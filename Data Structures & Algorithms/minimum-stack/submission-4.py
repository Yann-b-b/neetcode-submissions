class MinStack:

    def __init__(self):
        self.stack = []
        self.mini=[]

    def push(self, val: int) -> None:
        if self.stack == []:
            self.mini.append(val)
        elif val < self.mini[-1]:
            self.mini.append(val)
        else:
            self.mini.append(self.mini[-1])
        self.stack.append(val)
        
    def pop(self) -> None:
        self.mini = self.mini[:len(self.mini)-1]
        self.stack = self.stack[:len(self.stack)-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return (self.mini[-1])
