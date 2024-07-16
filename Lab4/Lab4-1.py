class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.stack)

    def display(self):
        print(self.stack)

obj1 = Stack()

while True:
    user_input = int(input("Enter a number to push onto the stack (-1 to terminate): "))
    if user_input == -1:
        break
    obj1.push(user_input)

obj1.display()

print("Popping")
popped_element = obj1.pop()
print(f"Popped element: {popped_element}")
obj1.display()

print("Peeking")
top_element = obj1.peek()
print(f"Top element: {top_element}")
