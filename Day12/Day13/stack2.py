class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,val):
        if len(self.stack)==5:
            return"Stack Over flow"
        else:
            self.stack.append(val)
            return("Pushed Element",val)
    def pop(self):
        if not self.stack:
            return"Stack Over flow"
        else:
            return self.stack.pop()
    
    def top(self):
        if not self.stack:
            return"Stack Under flow"
        else:
            return self.stack[-1]
    def peek(self):
        if not self.stack:
            return"Stack Under flow"
        else:
            return self.stack[-1]
stackObj=Stack()
print(stackObj.top())
ele=[10,20,30,40,50]
for i in ele:
    print(stackObj.push(i))
    print(stackObj.stack)

    