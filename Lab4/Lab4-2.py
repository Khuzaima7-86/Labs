class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    def size(self):
        return len(self.queue)

    def display(self):
        print(self.queue)

obj1 = Queue()

while True:
    user_input = int(input("Enter a number to enqueue onto the queue (-1 to terminate): "))
    if user_input == -1:
        break
    obj1.enqueue(user_input)


obj1.display()


print("Dequeueing")
dequeued_element = obj1.dequeue()
print(f"Dequeued element: {dequeued_element}")
obj1.display()

print("Peeking")
front_element = obj1.front()
print(f"Front element: {front_element}")
