class MinStack:

    def __init__(self):
        
        self.stack = []
        self.mini = float("inf")
        

    def push(self, val: int) -> None:
        
        if len(self.stack) == 0:
            self.stack.append(val)
            self.mini = val
            
        else:
            ele = self.stack[-1]
             
            if val < self.mini:
                self.stack.append(2*val - self.mini)
                self.mini = val
            else:
                self.stack.append(val)    
        
    def pop(self) -> None:
        
        if len(self.stack) == 0:
            return None
        ele = self.stack[-1]
        self.stack.pop()
        if ele < self.mini:
            self.mini = 2*self.mini - ele
            
        if len(self.stack) == 0:
            self.mini = float("inf")

    def top(self) -> int:
        ele = self.stack[-1]
        if ele < self.mini:
            return self.mini
        else:
            return ele
        

    def getMin(self) -> int:
        return self.mini
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()