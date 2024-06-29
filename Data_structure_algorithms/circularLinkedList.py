class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insertBeginning(self, data) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head.prev = new_node

    def insertEnd(self, data) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node

    def insertMiddle(self, data, index: int) -> None:
        if index < 0:
            print("Invalid position")
            return

        new_node = Node(data)

        if index == 0:
            self.insertBeginning(data)

        cur = self.head

        for _ in range(index - 1):
            if cur.next == self.head:
                print("Index out of bounds")
                return
            cur = cur.next

        new_node.next = cur.next
        new_node.prev = cur
        cur.next.prev = new_node
        cur.next = new_node

    def deleteNode(self, key) -> None:
        if self.head is None:
            return

        cur = self.head
        while True:
            if cur.data == key:
                if cur == self.head:
                    self.head = cur.next
                    self.tail.next = self.head
                    self.head.prev = self.tail
                elif cur == self.tail:
                    self.tail = cur.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                return

            cur = cur.next
            if cur == self.head:
                break

        print("Key not found")

    def search(self, key) -> bool:
        if self.head is None:
            return False

        cur = self.head
        while True:
            if cur.data == key:
                return True

            elif cur.next == self.head:
                break

            cur = cur.next
        return False

    def getLength(self) -> int:
        if self.head is None:
            return 0

        count = 1
        cur = self.head
        while cur.next is not self.head:
            count += 1
            cur = cur.next

        return count

    def display(self) -> None:
        if self.head is None:
            print("List is empty")
            return

        cur = self.head
        while True:
            print(cur.data, end=" <-> ")
            cur = cur.next
            if cur == self.head:
                break

        print("Head")


cdll = CircularLinkedList()
cdll.insertEnd(10)
cdll.insertEnd(20)
cdll.insertBeginning(5)
cdll.insertMiddle(15, 2)  # Insert 15 at position 2
cdll.display()  # Output: 5 <-> 10 <-> 15 <-> 20 <-> Head
print(cdll.search(10))  # Output: True
print(cdll.getLength())  # Output: 4
cdll.deleteNode(10)
cdll.display()  # Output: 5 <-> 15 <-> 20 <-> Head
