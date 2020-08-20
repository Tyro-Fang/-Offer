class StackWithMin:
    def __init__(self):
        self.stack=[]
        self.minStack=[]
        #初始化最小值最大，便于比较
        self.minVal=float('inf')
    def push(self,val):
        self.stack.append(val)
        if val<self.minVal:
            self.minStack.append(val)
            self.minVal=val
        else:
            self.minStack.append(self.minVal)
    def pop(self):
        if self.stack!=[]:
            if self.stack[-1]==self.minVal:
                self.minStack.pop()
            self.stack.pop()
    def min(self):
        return self.minVal



