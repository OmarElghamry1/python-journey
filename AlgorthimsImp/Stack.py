class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if self.is_empty():
            print("Empty")
            return
        return self.stack[-1]

    def push(self, num):
        self.stack.append(num)
        return

    def pop(self):
        if self.is_empty():
            print("Empty")
            return
        else:
            top_element = self.stack[-1]
            self.stack = self.stack[:-1]
        return top_element


if __name__ == "__main__":
    stk = Stack()
