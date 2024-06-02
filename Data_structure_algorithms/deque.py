class Deque:
    def __init__(self):
        self._values = []

    def isEmpty(self) -> bool:
        return len(self._values) == 0

    def addFront(self, value):
        self._values.insert(0, value)

    def addRear(self, value):
        self._values.append(value)

    def removeFront(self):
        if self.isEmpty():
            return None
        return self._values.pop(0)

    def removeRear(self):
        if self.isEmpty():
            return None
        return self._values.pop()

    def peekFront(self):
        if self.isEmpty():
            return None
        return self._values[0]

    def peekRear(self):
        if self.isEmpty():
            return None
        return self._values[-1]

    def __str__(self) -> str:
        return f"Deque: {self._values}"


deque = Deque()

# Add elements to the rear
deque.addRear(10)
deque.addRear(20)
deque.addRear(30)
print(deque)  # Deque: [10, 20, 30]

# Add elements to the front
deque.addFront(5)
deque.addFront(1)
print(deque)  # Deque: [1, 5, 10, 20, 30]

# Peek front and rear
print(deque.peekFront())  # 1
print(deque.peekRear())   # 30

# Remove elements from the front
print(deque.removeFront())  # 1
print(deque.removeFront())  # 5
print(deque)  # Deque: [10, 20, 30]

# Remove elements from the rear
print(deque.removeRear())  # 30
print(deque)  # Deque: [10, 20]

# Check if deque is empty
print(deque.isEmpty())  # False

# Remove remaining elements
deque.removeFront()
deque.removeFront()
print(deque)  # Deque: []
print(deque.isEmpty())  # Output: True
