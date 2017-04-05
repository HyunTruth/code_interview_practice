class Nodes:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)


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

    def __str__(self):
        value_list = []
        current = self.head
        while current is not None:
            value_list.append(current.value)
            current = current.next
        return str(value_list)

    def remove_item(self, item):
        if self.head.value == item:
            self.remove_head()
        else:
            current = self.head
            while current is not None:
                if current.next.value == item:
                    next_node = current.next.next
                    current.next.next = None
                    current.next = next_node
                    return self
                current = current.next


a = LinkedList()

a.add_to_tail(1)
a.add_to_tail(2)
a.add_to_tail(3)
a.add_to_tail(4)
a.add_to_tail(5)
a.add_to_tail(6)

print(a.remove_item(5))