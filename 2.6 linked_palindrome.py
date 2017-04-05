class Node:
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
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            temp = self.tail
            self.tail = new_node
            temp.next = self.tail
            self.counter += 1

    def remove_head(self):
        if self.head is None:
            raise NotImplementedError('No nodes in the list')
        else:
            self.head = self.head.next

    def __str__(self):
        value_list = []
        current = self.head
        if self.head is not None:
            while current.next is not None:
                value_list.append(current.value)
                current = current.next
            value_list.append(current.value)
        return str(value_list)

    def __len__(self):
        return self.counter

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev






a = LinkedList()
a.add_to_tail(7)
a.add_to_tail(1)
a.add_to_tail(7)


b = LinkedList()
b.add_to_tail(5)
b.add_to_tail(9)
b.add_to_tail(2)

print(b)

b.reverse()

print(b)