class BinaryTree():

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.order = []

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_node_value(self, value):
        self.value = value

    def get_node_value(self):
        return self.value

    def add_left_child(self, value):
        if self.left is None:
            self.left = BinaryTree(value)
        else:
            tree = BinaryTree(value)
            tree.left = self.left
            self.left = tree

    def add_right_child(self, value):
        if self.right is None:
            self.right = BinaryTree(value)
        else:
            tree = BinaryTree(value)
            tree.right = self.right
            self.right = tree

    def __str__(self):
        return str(self.get_node_value())

    def check_bst(self):
        if self is not None:
            self.is_bst(self)
        return self.is_sorted()

    def is_sorted(self, key=lambda x: x):
        for i, el in enumerate(self.order[1:]):
            if key(el) < key(self.order[i]):  # i is the index of the previous element
                return False
        return True

    def is_bst(self, node):
        if node.left is not None:
            self.is_bst(node.left)

        self.order.append(node.value)
        print(node.value)

        if node.right is not None:
            self.is_bst(node.right)



def print_tree(bt):
    if bt is not None:
        print_tree(bt.left)
        print(bt)
        print_tree(bt.right)


myTree = BinaryTree(3)
myTree.add_left_child(2)
myTree.add_right_child(6)
myTree.add_right_child(8)

print(myTree.check_bst())
print_tree(myTree)