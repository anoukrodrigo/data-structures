# Define the Node class for the stack (linked list node)
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Define the Stack class using linked list
class Stack:
    def __init__(self):
        self.head = None

    # Method to check if the stack is empty
    def is_empty(self):
        return self.head is None

    # Method to push (add) a new element onto the stack
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Method to pop (remove) the top element from the stack and return its value
    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        else:
            popped_data = self.head.data
            self.head = self.head.next
            return popped_data

    # Method to display the elements currently in the stack
    def display(self):
        current = self.head
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack:")
            while current:
                print(current.data)
                current = current.next

# Main function to demonstrate stack operations
if __name__ == "__main__":
    stack = Stack()

    while True:
        print("\n1. Push element onto the stack")
        print("2. Pop element from the stack")
        print("3. Display stack")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = input("Enter data to push onto the stack: ")
            stack.push(data)
            print(f"Pushed '{data}' onto the stack.")
        elif choice == 2:
            popped_data = stack.pop()
            if popped_data is not None:
                print(f"Popped element: {popped_data}")
        elif choice == 3:
            stack.display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
