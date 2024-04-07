#Min Stack
class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val):
        if (self.min and val < self.min) or self.min is None:
            self.stack.append([val, val])
            self.min = val
        else:
            self.stack.append([val, self.min])

    def pop(self):
        self.stack.pop()
        if self.stack:
            self.min = self.stack[-1][1]
        else:
            self.min = None

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.min
    
class MinStackNeet(object):
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]

mystack = MinStackNeet()
mystack.push(5)
mystack.push(-2)
mystack.push(8)
mystack.push(-7)
mystack.push(13)
mystack.push(9)
print(mystack.top())
print(mystack.getMin())
mystack.pop()
print(mystack.top())
mystack.pop()
mystack.pop()
print(mystack.getMin())