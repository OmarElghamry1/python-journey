class Node:
    def __init__(self, data=None, Next=None, Prev=None):
        self.data = data
        self.Next = Next
        self.Prev = Prev

    def set_prev(self, Prev):
        self.Prev = Prev

    def set_next(self, Next):
        self.Next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        if self.head == None:  # First insertion
            node = Node(data, self.head, None)
            self.tail = node
        else:
            node = Node(data, self.head, None)
            self.head.set_prev(node)

        self.head = node
        return

    def insert_at_end(self, data):
        if self.head == None:
            self.insert_at_beginning(data)
            return

        else:
            node = Node(data, None, self.tail)
            self.tail.set_next(node)
            self.tail = node

        return

    def printForward(self):
        if self.head == None:
            print("Double LinkedList is Empty")
            return

        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.Next

        print(llstr)

    def printBackward(self):
        if self.tail == None:
            print("Double Linked List is empty")
            return
        itr = self.tail
        llstr = ""
        while itr:
            llstr += "<--" + str(itr.data)
            itr = itr.Prev

        print(llstr)

    def printHead(self):
        print(f"Head: {self.head.data}")

    def printTail(self):
        print(f"Tail: {self.tail.data}")


if __name__ == "__main__":
    dl = DoubleLinkedList()
    dl.insert_at_beginning("A")
    dl.insert_at_beginning("B")
    dl.insert_at_beginning("C")

    dl.printForward()
    dl.printBackward()
    dl.printHead()
    dl.printTail()
