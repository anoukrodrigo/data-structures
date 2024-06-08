class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = -1
        self.tail = -1

    def is_full(self):
        return (self.tail + 1) % self.size == self.head

    def is_empty(self):
        return self.head == -1

    def enqueue(self, element):
        if self.is_full():
            print("Queue is full, cannot enqueue.")
            return
        if self.is_empty():
            self.head = 0
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = element
        print(f"Enqueued: {element}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue.")
            return None
        element = self.queue[self.head]
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.size
        print(f"Dequeued: {element}")
        return element

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            if self.tail >= self.head:
                print("Current FIFO queue:", self.queue[self.head:self.tail + 1])
            else:
                print("Current FIFO queue:", self.queue[self.head:self.size] + self.queue[0:self.tail + 1])

def main():
    size = int(input("Enter the size of the circular FIFO queue: "))
    fifo_queue = CircularQueue(size)

    while True:
        user_input = input("Enter an element to enqueue, 'dequeue' to dequeue, or 'exit' to stop: ").strip()

        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'dequeue':
            fifo_queue.dequeue()
        else:
            fifo_queue.enqueue(user_input)

        fifo_queue.display()

    print("Queue processing complete.")

if __name__ == "__main__":
    main()
