import sys


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        print("before insertion", self.head)
        node = Node(data, self.head)
        self.head = node
        print("after insertion", self.head)

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = Node(data, None)  # type: ignore

    def printLinkList(self):
        if self.head is None:
            print("Linked List is empty")
        i = self.head
        string = ""

        while i:
            string += str(i.data) + "-->"
            i = i.next

        print(string)

    def insert_list(self, data_list):
        for data in data_list:
            self.insert_at_end(data)
        return

    def remove_at(self, i):  # removes at intended index
        if i >= self.get_length() or i < 0:
            print("Out of index")
            return

        if i == 0:
            self.head = self.head.next
            return

        cnt = 0
        start = self.head
        while start:
            if cnt == i - 1:
                start.next = start.next.next
                break
            start = start.next
            cnt += 1

    def get_length(self):
        cnt = 0
        beginning = self.head
        while beginning:
            beginning = beginning.next
            cnt += 1

        return cnt

    def insert_at(self, i, data):
        if i < 0 or i >= self.get_length():
            raise Exception("YOOO Stop out of index")

        if i == 0:
            self.insert_at_beginning(data)
            return

        if i == (self.get_length() - 1):
            self.insert_at_end(data)
            return

        itr = self.head
        cnt = 0
        while itr:
            if cnt == i - 1:
                itr.next = Node(data, itr.next)
                return

            itr = itr.next
            cnt += 1

        return

    def insert_after_value(self, data_after, data_insertion):
        if self.get_length() == 0:
            print("LinkedList is Empty")
            return

        if self.head.data == data_after:
            self.insert_at(1, data_insertion)
            return

        itr = self.head.next  # Since we checked already for fist element
        cnt = 1

        while itr:
            if cnt == self.get_length() - 1 and itr.data == data_after:
                self.insert_at_end(data_insertion)
                return

            if itr.data == data_after:
                self.insert_at(cnt + 1, data_insertion)
                return

            itr = itr.next
            cnt += 1

        print("Data Not found!")
        return

    def remove_by_value(self, data_to_removed):
        if self.get_length() == 0:
            print("LinkedList is Empty")
            return
        if self.head.data == data_to_removed:
            self.remove_at(0)
            return

        itr = self.head.next  # Since we checked already for fist element
        cnt = 1

        while itr:
            if itr.data == data_to_removed:
                self.remove_at(cnt)
                return

            itr = itr.next
            cnt += 1

        print("Data Not found!")
        return

    def printHead(self):
        print(f"Head is {self.head.data}")


if __name__ == "__main__":
    # linkedlist = LinkedList()
    # linkedlist.insert_at_end("5")
    # linkedlist.insert_at_end("4")
    # linkedlist.insert_at_end("3")
    # linkedlist.insert_at_end("2")
    # linkedlist.insert_at_end("1")
    # linkedlist.insert_at_beginning("1")
    # linkedlist.insert_at_beginning("2")
    # linkedlist.insert_at_beginning("3")
    # linkedlist.in1sert_at_end('This is the end')
    # pizza = ["PapaJohns", "Dominos", "TheChef"]
    # linkedlist.insert_list(pizza)
    # print("Before")
    # linkedlist.printLinkList()
    # print("After")
    # linkedlist.printLinkList()
    # print(f"Length of LinkedList: {linkedlist.get_length()}")
    # print(sys.version)
    # print(sys.executable)
    pass
