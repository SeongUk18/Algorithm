class Node:
    def __init__(self, data=None):
        self._data = data
        self._next = None

    def setNext(self, next):
        self._next = next

    def getNext(self):
        return self._next

    def getData(self):
        return self._data


class SinglyLinkedList:
    def __init__(self):
        self._head = None

    def insertBeginning(self, data):
        new_node = Node(data)
        new_node.setNext(self._head)
        self._head = new_node

    def insertEnd(self, data):
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
            return
        last = self._head
        while last.getNext():
            last = last.getNext()
        last.setNext(new_node)

    def insertMiddle(self, data, index):
        if index < 0:
            print("Invalid position")
            return
        new_node = Node(data)
        if index == 0:
            new_node.setNext(self._head)
            self._head = new_node
            return
        cur = self._head
        for i in range(index - 1):
            if cur is None:
                print("Index out of bounds")
                return
            cur = cur.getNext()
        if cur is None:
            print("Index out of bounds")
            return
        new_node.setNext(cur.getNext())
        cur.setNext(new_node)

    def deleteNode(self, key):
        temp = self._head

        if temp is not None:
            if temp.getData() == key:
                self._head = temp.getNext()
                temp = None
                return

        while temp is not None:
            if temp.getData() == key:
                break
            prev = temp
            temp = temp.getNext()

        if temp == None:
            return

        prev.setNext(temp.getNext())
        temp = None

    def search(self, key):
        cur = self._head
        while cur is not None:
            if cur.getData() == key:
                return True
            cur = cur.getNext()
        return False

    def getLength(self) -> int:
        count = 0
        cur = self._head
        while cur:
            count += 1
            cur = cur.getNext()
        return count

    def display(self):
        cur = self._head
        while cur:
            print(cur.getData(), end=" -> ")
            cur = cur.getNext()
        print("None")


sll = SinglyLinkedList()
sll.insertEnd(10)
sll.insertEnd(20)
sll.insertBeginning(5)
sll.insertMiddle(15, 2)  # Insert 15 at position 2
sll.display()  # 5 -> 10 -> 15 -> 20 -> None
print(sll.search(10))  # True
print(sll.getLength())  # 4
sll.deleteNode(10)
sll.display()  # 5 -> 15 -> 20 -> None
