class MultiStacks:
    def __init__(self, stack_size):
        self.array = [None] * stack_size * 3
        self.stack_size = stack_size
        self.stack1_bot = 0
        self.stack1_top = self.stack_size + self.stack1_bot
        self.stack2_bot =  self.stack1_top
        self.stack2_top = self.stack_size + self.stack2_bot
        self.stack3_bot = self.stack2_top
        self.stack3_top = self.stack_size + self.stack3_bot

        self.stack1_idx = 0
        self.stack2_idx = self.stack1_idx + self.stack_size
        self.stack3_idx = self.stack2_idx + self.stack_size

    def __str__(self):
        return str(self.array)

    def push_stack1(self, item):
        if self.stack1_idx == self.stack1_top:
            raise IndexError('Stack is full!')
        else:
            self.array[self.stack1_idx] = item
            self.stack1_idx += 1

    def pop_stack1(self):
        if self.stack1_idx <= self.stack1_bot:
            raise IndexError('Stack is empty!')
        else:
            self.stack1_idx -= 1
            temp = self.array[self.stack1_idx]
            self.array[self.stack1_idx] = None
            return temp

    def push_stack2(self, item):
        if self.stack2_idx == self.stack2_top:
            raise IndexError('Stack is full!')
        else:
            self.array[self.stack2_idx] = item
            self.stack2_idx += 1

    def pop_stack2(self):
        if self.stack2_idx <= self.stack2_bot:
            raise IndexError('Stack is empty!')
        else:
            self.stack2_idx -= 1
            temp = self.array[self.stack2_idx]
            self.array[self.stack2_idx] = None
            return temp

    def push_stack3(self, item):
        if self.stack3_idx == self.stack3_top:
            raise IndexError('Stack is full!')
        else:
            self.array[self.stack3_idx] = item
            self.stack3_idx += 1

    def pop_stack3(self):
        if self.stack3_idx <= self.stack3_bot:
            raise IndexError('Stack is empty!')
        else:
            self.stack3_idx -= 1
            temp = self.array[self.stack3_idx]
            self.array[self.stack3_idx] = None
            return temp

a = MultiStacks(3)
a.push_stack1(5)
a.push_stack1(6)
a.push_stack1(7)
a.pop_stack1()
a.push_stack2(1)
a.push_stack2(3)
a.pop_stack2()
a.push_stack3(7)


print(a)