# Create a FIFO queue
fifo_queue = []

while True:
    # Take user input for enqueue or dequeue operation
    user_input = input("Enter an element to enqueue, 'dequeue' to dequeue, or 'exit' to stop: ").strip()

    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        break

    # Enqueue operation
    elif user_input.lower() != 'dequeue':
        fifo_queue.append(user_input)
        print(f"Enqueued: {user_input}")

    # Dequeue operation
    elif user_input.lower() == 'dequeue':
        if fifo_queue:
            element = fifo_queue.pop(0)
            print(f"Dequeued: {element}")
        else:
            print("Queue is empty, cannot dequeue.")

    # Show the current state of the FIFO queue
    print(f"Current FIFO queue: {fifo_queue}")

print("Queue processing complete.")
