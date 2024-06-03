class CircularQueue:
    def __init__(self, size: int):
        self._size = size
        self._values = [None for _ in range(self._size)]
        self._front_pointer = -1
        self._rear_pointer = -1

    def isFull(self) -> bool:
        if (self._rear_pointer + 1) % self._size == self._front_pointer:
            return True
        else:
            return False

    def isEmpty(self) -> bool:
        if self._front_pointer == -1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isFull():
            print("Queue is Full")
            return
        if self.isEmpty():
            self._front_pointer = 0
        self._rear_pointer = (self._rear_pointer + 1) % self._size
        self._values[self._rear_pointer] = value

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        result = self._values[self._front_pointer]
        self._values[self._front_pointer] = None

        if self._front_pointer == self._rear_pointer:
            self._front_pointer = self._rear_pointer = -1
        else:
            self._front_pointer = (self._front_pointer + 1) % self._size
        return result

    def front(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        return self._values[self._front_pointer]

    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Queue: ", end='')
            i = self._front_pointer
            while True:
                print(self._values[i], end=' ')
                if i == self._rear_pointer:
                    break
                i = (i + 1) % self._size
            print()


cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.display()  # Queue: 10 20 30 40
print(cq.dequeue())  # 10
cq.display()  # Queue: 20 30 40
cq.enqueue(50)
cq.enqueue(60)
cq.display()  # Queue: 20 30 40 50 60
cq.enqueue(70)  # Queue is Full
print(cq.front())  # 20
