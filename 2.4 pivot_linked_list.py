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

    def pivot_linked_list(self, item):
        if len(self) <= 1:
            return self
        else:
            pre = LinkedList()
            post = LinkedList()
            mid = None
            current = self.head
            while current is not None:
                if current.value > item:
                    post.add_to_tail(current.value)
                if current.value < item:
                    pre.add_to_tail(current.value)
                if current.value == item:
                    mid = Node(current.value)
                current = current.next
            print(pre, post)
            pre.tail.next = mid
            mid.next = post.head
            return pre





a = LinkedList()

a.add_to_tail(6)
a.add_to_tail(3)
a.add_to_tail(8)
a.add_to_tail(1)
a.add_to_tail(5)
a.add_to_tail(9)
# print(a)

print(a.pivot_linked_list(5))
print(a)