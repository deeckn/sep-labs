class OutOfRangeError(Exception):
    pass


class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            raise OutOfRangeError("Stack is empty, unable to do pop operation")
        return self.stack.pop()

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def size(self) -> int:
        return len(self.stack)

    def peek(self):
        if self.is_empty():
            raise OutOfRangeError(
                "Stack is empty, unable to do peek operation")
        return self.stack[len(self.stack)-1]
