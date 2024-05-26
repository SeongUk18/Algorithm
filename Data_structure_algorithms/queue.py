class Queue:
    def __init__(self):
        self._values = []

    def enqueue(self, value):
        self._values.append(value)

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            return self._values.pop(0)

    def front(self):
        if self.isEmpty():
            return None
        else:
            return self._values[0]

    def isEmpty(self) -> bool:
        if len(self._values) == 0:
            return True
        else:
            return False

    def size(self) -> int:
        return len(self._values)

    def __str__(self) -> str:
        return f"Queue: {self._values}"


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)  # Queue: [1, 2, 3]
print(queue.dequeue())  # 1
print(queue.front())  # 2
print(queue.isEmpty())  # False
print(queue.size())  # 2
