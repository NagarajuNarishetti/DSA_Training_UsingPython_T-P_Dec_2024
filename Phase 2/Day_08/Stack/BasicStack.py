class Stack:
    def __init__(self):
        self.stack = []

    def add(self, data):
        self.stack.append(data)

    def removal(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return "Stack is empty"

    def size(self):
        return len(self.stack)

s = Stack()
s.add(10)
s.add(20)
s.add(30)
print(s.stack)
print(s.size)
s.removal()
s.removal()
s.removal()
print(s.removal())
print(s.stack)