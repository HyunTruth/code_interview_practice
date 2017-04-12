class Nodes:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0

    def add_to_head(self, value):
        new_node = Nodes(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            temp = self.head
            new_node.next = temp
            self.head = new_node
        self.counter += 1

    def add_to_tail(self, value):
        new_node = Nodes(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            temp = self.tail
            temp.next = new_node
            self.tail = new_node
        self.counter += 1

    def remove_head(self):
        if self.head is None:
            return NotImplementedError('head underflow')
        else:
            temp = self.head
            del self.head
            self.head = temp.next
            self.counter -= 1
            return temp.value

    def __len__(self):
        return self.counter


class Stack(LinkedList):

    def __init__(self):
        super(Stack, self).__init__()
        self.mins = []
        self.min = None

    def push(self, value):
        self.mins.append(self.min)
        if self.min is None or self.min > value:
            self.min = value
        return self.add_to_head(value)

    def pop(self):
        self.min = self.mins.pop()
        return self.remove_head()

    def min(self):
        return self.min


a = Stack()
a.push(1)
a.push(2)
a.push(3)
print(a.pop())
print(a.min)