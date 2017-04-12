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
        self.length = 0

    def push(self, value):
        self.length += 1
        return self.add_to_head(value)

    def pop(self):
        self.length -= 1
        return self.remove_head()

    def __len__(self):
        return self.length


class SetOfStacks:

    def __init__(self):
        self.sets = []
        self.stack_size = 3
        self.sets.append(Stack())

    def push(self, value):
        stack = self.sets[len(self.sets) - 1]
        if len(stack) < self.stack_size:
            return stack.push(value)
        else:
            new_stack = Stack()
            new_stack.push(value)
            return self.sets.append(new_stack)

    def pop(self):
        stack = self.sets[len(self.sets) - 1]
        if len(stack) == 1:
            last_stack = self.sets.pop()
            return last_stack.pop()
        else:
            return stack.pop()


a = SetOfStacks()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)

print(a.pop())
print(a.sets)
print(a.pop())
print(a.pop())
print(a.sets)