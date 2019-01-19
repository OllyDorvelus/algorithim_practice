class Node:
    def __init__(self, data):
        self.data = data


class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def getLength(self):
        return len(self.stack)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            print("Stack is empty, cannot pop")
            return -1
        return self.stack.pop()

    def peek(self):
        lastIndex = len(self.stack) - 1
        return self.stack[lastIndex]


myStack = Stack()
myStack.push(3)
myStack.push(5)
print(myStack.peek())
print(myStack.pop())
print(myStack.peek())
print(myStack.pop())
print(myStack.pop())
