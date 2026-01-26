class Queue:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return True if len(self.list) == 0 else False

    def peek(self):
        if self.is_empty():
            return "Empty"
        else:
            return self.list[0]

    def push(self, val):
        """Validation"""
        self.list.append(val)

    def pop(self):
        first_element = self.list[0]
        self.list = self.list[1:]
        return first_element

    def Str(self):
        return str(self.list)


if __name__ == "__main__":
    q = Queue()
