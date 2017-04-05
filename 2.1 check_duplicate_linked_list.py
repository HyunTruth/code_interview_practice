class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            temp = self.tail
            self.tail = new_node
            temp.next = self.tail
            self.counter += 1

    def remove_head(self):
        if self.head == None:
            raise NotImplementedError('No nodes in the list')
        else:
            self.head = self.head.next

    def __str__(self):
        value_list = []
        current = self.head
        while current.next is not None:
            value_list.append(current.value)
            current = current.next
        value_list.append(current.value)
        return str(value_list)

    def remove_duplicate(self):
        dict = {}
        current = self.head
        while current is not None:
            if current.value in dict:
                prev.next = current.next
            else:
                dict[current.value] = True
                prev = current
            current = current.next

a = LinkedList()

a.add_to_tail(1)
a.add_to_tail(2)
a.add_to_tail(3)
a.add_to_tail(4)
a.add_to_tail(5)
a.add_to_tail(6)
a.remove_head()
a.remove_head()

a.add_to_tail(6)

print(a.remove_duplicate())
print(a)
