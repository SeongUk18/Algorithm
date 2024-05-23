class Stack:
    def __init__(self):
        self._values = []

    def push(self, value: int):
        self._values.append(value)

    def pop(self) -> int:
        if not self.isEmpty():
            return self._values.pop()
        else:
            return None

    def top(self) -> int:
        if not self.isEmpty():
            return self._values[-1]
        else:
            return None

    def isEmpty(self) -> bool:
        if len(self._values) == 0:
            return True
        else:
            return False

    def size(self) -> int:
        return len(self._values)

    def __str__(self) -> str:
        return f"Stack: {self._values}"


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)  # Stack: [1, 2, 3]
print(stack.pop())  # 3
print(stack.top())  # 2
print(stack.isEmpty())  # False
print(stack.size())  # 2
