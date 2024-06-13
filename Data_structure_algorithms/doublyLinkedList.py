class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def insertEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def insertMiddle(self, data, index):
        if index < 0:
            print("Invalid position")
            return
        new_node = Node(data)
        if index == 0:
            self.insertBeginning(data)
            return
        cur = self.head
        for i in range(index - 1):
            if cur is None:
                print("Index out of bounds")
                return
            cur = cur.next
        if cur is None:
            print("Index out of bounds")
            return
        new_node.next = cur.next
        new_node.prev = cur
        if cur.next is not None:
            cur.next.prev = new_node
        cur.next = new_node
        if new_node.next is None:
            self.tail = new_node

    def deleteNode(self, key):
        temp = self.head
        while temp is not None:
            if temp.data == key:
                if temp.prev is not None:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next is not None:
                    temp.next.prev = temp.prev
                else:
                    self.tail = temp.prev
                return
            temp = temp.next
        print("Key not found")

    def search(self, key):
        cur = self.head
        while cur is not None:
            if cur.data == key:
                return True
            cur = cur.next
        return False

    def getLength(self) -> int:
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=" <-> ")
            cur = cur.next
        print("None")


# Example usage
dll = DoublyLinkedList()
dll.insertEnd(10)
dll.insertEnd(20)
dll.insertBeginning(5)
dll.insertMiddle(2, 15)  # Insert 15 at position 2
dll.display()  # Output: 5 <-> 10 <-> 15 <-> 20 <-> None
print(dll.search(10))  # Output: True
print(dll.getLength())  # Output: 4
dll.deleteNode(10)
dll.display()  # Output: 5 <-> 15 <-> 20 <-> None

