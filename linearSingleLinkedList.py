# Define the Node class
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to insert a new node at the beginning of the linked list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Method to insert a new node at the end of the linked list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Method to delete a node with a given value from the linked list
    def delete_node(self, key):
        current = self.head

        # If head node itself holds the key to be deleted
        if current is not None and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the key to be deleted, keep track of the previous node
        prev = None
        while current is not None and current.data != key:
            prev = current
            current = current.next

        # If key was not present in linked list
        if current is None:
            print("Data not found in the list.")
            return

        # Unlink the node from the linked list
        prev.next = current.next
        current = None

    # Method to display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Main function to demonstrate the linked list operations
if __name__ == "__main__":
    linked_list = LinkedList()

    while True:
        print("\n1. Insert at beginning")
        print("2. Insert at end")
        print("3. Delete node by value")
        print("4. Display list")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = input("Enter data to insert at beginning: ")
            linked_list.insert_at_beginning(data)
        elif choice == 2:
            data = input("Enter data to insert at end: ")
            linked_list.insert_at_end(data)
        elif choice == 3:
            data = input("Enter data to delete: ")
            linked_list.delete_node(data)
        elif choice == 4:
            print("Linked List:")
            linked_list.display()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
