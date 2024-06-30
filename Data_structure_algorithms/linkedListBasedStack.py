class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None


class LinkedListBasedStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data) -> None:
        new_data = Node(data)
        if self.is_empty():
            self.top = new_data
        else:
            new_data.prev = self.top
            self.top = new_data

        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            cur = self.top
            self.top = self.top.prev
            self.size -= 1
            return cur.data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self) -> bool:
        return self.size == 0

    def get_size(self) -> int:
        return self.size

    def display(self) -> None:
        cur = self.top
        while True:
            if cur is None:
                print("None")
                return
            print(cur.data, "-> ", end="")
            cur = cur.prev


stack = LinkedListBasedStack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()  # Output: 30 -> 20 -> 10 -> None
print(stack.pop())  # Output: 30
print(stack.peek())  # Output: 20
print(stack.is_empty())  # Output: False
print(stack.get_size())  # Output: 2
stack.display()  # Output: 20 -> 10 -> None
