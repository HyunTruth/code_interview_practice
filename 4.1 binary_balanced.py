class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.value)

class BinaryTree:
    def __init__(self):
        self.root = None

    def getroot(self):
        return self.root

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        if value < node.value :
            if node.left is not None:
                self._add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right is not None:
                self._add(value, node.right)
            else:
                node.right = Node(value)

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print(str(node.value) + ' ')
            self._print_tree(node.right)

    def is_balanced(self):
        if self.check_height(self.root) == -1:
            return False
        else:
            return True

    def check_height(self, node):
        if node is None:
            return 0

        left_height = self.check_height(node.left)
        if left_height == -1:
            return -1

        right_height = self.check_height(node.right)
        if right_height == -1:
            return -1

        height_diff = abs(left_height - right_height)
        if height_diff > 1:
            return -1
        return max(left_height, right_height) + 1


tree = BinaryTree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.add(1)

print(tree.is_balanced())




