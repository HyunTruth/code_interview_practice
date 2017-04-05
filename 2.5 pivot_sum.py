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

    def __add__(self, other):
        v1 = self.head
        v2 = other.head
        carry = 0

        while v1 is not None:
            val = ((v1.value + v2.value)%10) + carry
            carry = (v1.value + v2.value) // 10
            v1.value = val
            v1 = v1.next
            v2 = v2.next

        current = self.head

        result = 0
        digit = 0

        while current is not None:
            result += (current.value * (10**digit))
            digit += 1
            current = current.next

        return result





a = LinkedList()
a.add_to_tail(7)
a.add_to_tail(1)
a.add_to_tail(6)


b = LinkedList()
b.add_to_tail(5)
b.add_to_tail(9)
b.add_to_tail(2)

print(a + b)