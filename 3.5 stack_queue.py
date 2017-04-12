class Nodes:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0

    def push(self, value):
        new_node = Nodes(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            temp = self.head
            new_node.next = temp
            self.head = new_node
        self.counter += 1

    def pop(self):
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


class Queue:
    def __init__(self):
        self.main = Stack()
        self.rev = Stack()

    def enqueue(self, value):
        self.main.push(value)

    def dequeue(self):
        if len(self.main) <= 0:
            return NotImplementedError('no queued content')
        else:
            while len(self.main) > 0:
                self.rev.push(self.main.pop())
            temp = self.rev.pop()
            while len(self.rev) > 0:
                self.main.push(self.rev.pop())
            return temp

    def __len__(self):
        return len(self.main)

a = Queue()

a.enqueue(1)
a.enqueue(2)
a.enqueue(3)

print(a.dequeue())
print(a.dequeue())