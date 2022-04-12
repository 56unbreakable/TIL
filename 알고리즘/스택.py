class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def __len__(self):
        return len(self.stack)

    def pop(self):
        if self.__len__() > 0:
            a = self.stack[-1]
            del self.stack[-1]
        else:
            a = "empty stack"
        return a

    def size(self):
        print(self.__len__())

    def empty(self):
        if self.__len__() > 0:
            e = False
        else:
            e = True
        return e

    def top(self):
        if self.__len__() > 0:
            a = self.stack[-1]
        else:
            a = "empty stack"
        return a