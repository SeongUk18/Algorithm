from collections import deque


class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.val = key


class BinaryTree:
    def __init__(self, root=None) -> None:
        self.root = root

    def insert(self, key) -> None:
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, key)

    def _insert(self, root, key) -> None:
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def preorder(self, node):
        if node:
            print(node.val, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val, end=" ")
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val, end=" ")

    def level_order(self):
        if self.root is None:
            return
        q = deque()
        q.append(self.root)
        while q:
            cur = q.popleft()
            print(cur.val, end=" ")
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)


bt = BinaryTree()
bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.insert(2)
bt.insert(7)
bt.insert(12)
bt.insert(18)

print("Preorder traversal:")
bt.preorder(bt.root)  # Output: 10 5 2 7 15 12 18

print("\nInorder traversal:")
bt.inorder(bt.root)  # Output: 2 5 7 10 12 15 18

print("\nPostorder traversal:")
bt.postorder(bt.root)  # Output: 2 7 5 12 18 15 10

print("\nLevel order traversal:")
bt.level_order()  # Output: 10 5 15 2 7 12 18
