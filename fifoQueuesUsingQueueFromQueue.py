from queue import Queue

# Create a FIFO queue
fifo_queue = Queue()

while True:
    # Take user input for enqueue or dequeue operation
    user_input = input("Enter an element to enqueue, 'dequeue' to dequeue, or 'exit' to stop: ").strip()

    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        break

    # Enqueue operation
    elif user_input.lower() != 'dequeue':
        fifo_queue.put(user_input)
        print(f"Enqueued: {user_input}")

    # Dequeue operation
    elif user_input.lower() == 'dequeue':
        if not fifo_queue.empty():
            element = fifo_queue.get()
            print(f"Dequeued: {element}")
        else:
            print("Queue is empty, cannot dequeue.")

    # Show the current state of the FIFO queue
    temp_list = list(fifo_queue.queue)
    print(f"Current FIFO queue: {temp_list}")

print("Queue processing complete.")
