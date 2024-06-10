# Define the Node class for the queue (linked list node)
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Define the Queue class using linked list
class Queue:
    def __init__(self):
        self.front = None  # Points to the front of the queue (head)
        self.rear = None   # Points to the rear of the queue (tail)

    # Method to check if the queue is empty
    def is_empty(self):
        return self.front is None

    # Method to enqueue (add) a new element into the queue
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    # Method to dequeue (remove) an element from the front of the queue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        else:
            dequeued_data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return dequeued_data

    # Method to display the elements currently in the queue
    def display(self):
        current = self.front
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue:")
            while current:
                print(current.data)
                current = current.next

# Main function to demonstrate queue operations
if __name__ == "__main__":
    queue = Queue()

    while True:
        print("\n1. Enqueue element into the queue")
        print("2. Dequeue element from the queue")
        print("3. Display queue")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = input("Enter data to enqueue into the queue: ")
            queue.enqueue(data)
            print(f"Enqueued '{data}' into the queue.")
        elif choice == 2:
            dequeued_data = queue.dequeue()
            if dequeued_data is not None:
                print(f"Dequeued element: {dequeued_data}")
        elif choice == 3:
            queue.display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
