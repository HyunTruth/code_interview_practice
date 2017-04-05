class Nodes:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0

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

    def linked_list_nth(self, n):
        if len(self) == 0:
            return IndexError('no data available')
        if n == 0:
            return self.tail.value
        else:
            node1 = self.head
            stack = []
            while node1.next is not None:
                stack.append(node1)
                node1 = node1.next
            return stack[len(stack) - n].value



a = LinkedList()

a.add_to_tail(1)
a.add_to_tail(2)
a.add_to_tail(3)
a.add_to_tail(4)
a.add_to_tail(5)
a.add_to_tail(6)

print(a.linked_list_nth(1))