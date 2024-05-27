# Stack implementation using list
stack = []

# Function to push elements onto the stack
def push(stack, item):
    stack.append(item)

# Function to pop elements from the stack
def pop(stack):
    if stack:
        return stack.pop()
    else:
        print("Stack is empty!")
        return None

# Get user inputs
while True:
    action = input("Enter 'push' to add an element, 'pop' to remove an element, or 'quit' to exit: ").strip().lower()

    if action == 'push':
        item = input("Enter the element to push onto the stack: ")
        push(stack, item)
        print(f"Pushed {item} onto the stack.")
    elif action == 'pop':
        item = pop(stack)
        if item is not None:
            print(f"Popped {item} from the stack.")
    elif action == 'quit':
        print("Exiting.")
        break
    else:
        print("Invalid action. Please enter 'push', 'pop', or 'quit'.")

# Print the final state of the stack
print("Final stack:", stack)
