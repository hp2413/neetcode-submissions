class MinStack:

    def __init__(self):
        self.minVal = float('inf')
        self.stk = []


    def push(self, val: int) -> None:
        if len(self.stk) == 0 or self.minVal > val:
            self.stk.append(self.minVal)
            self.minVal = val
        self.stk.append(val)

    def pop(self) -> None:
        val = self.stk.pop()
        if self.minVal == val:
            self.minVal = self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minVal
        


class MinStack:

    def __init__(self):
        self.arr = []
        self.min = -(2**31)
        
    def push(self, val: int) -> None:
        if len(self.arr) == 0 or val <= self.min:
            self.arr.append(self.min)
            self.min = val
        self.arr.append(val)

    def pop(self) -> None:
        val = self.arr.pop()
        if val == self.min:
            self.min = self.arr.pop()

    def top(self) -> int:
        return self.arr[len(self.arr)-1]

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
