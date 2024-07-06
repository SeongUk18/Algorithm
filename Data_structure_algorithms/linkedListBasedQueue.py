class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedListBasedQueue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data) -> None:
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None

        delete_data = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None

        self.size -= 1

        return delete_data.data

    def peek_front(self):
        return self.front.data

    def peek_rear(self):
        return self.rear.data

    def is_empty(self) -> bool:
        return self.size == 0

    def get_size(self) -> int:
        return self.size

    def display(self) -> None:
        if self.is_empty():
            print("Queue is empty")
            return
        cur = self.front
        while cur:
            print(cur.data, "->", end=" ")
            cur = cur.next
        print("None")


queue = LinkedListBasedQueue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()  # Output: 10 -> 20 -> 30 -> None
print(queue.dequeue())  # Output: 10
print(queue.peek_front())  # Output: 20
print(queue.peek_rear())  # Output: 30
print(queue.is_empty())  # Output: False
print(queue.get_size())  # Output: 2
queue.display()  # Output: 20 -> 30 -> None
