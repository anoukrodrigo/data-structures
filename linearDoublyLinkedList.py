# Define the Node class for doubly linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

# Define the DoublyLinkedList class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Method to insert a new node at the beginning of the linked list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Method to insert a new node at the end of the linked list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    # Method to delete a node with a given value from the linked list
    def delete_node(self, key):
        current = self.head

        # Case 1: If the node to be deleted is the head node
        if current is not None and current.data == key:
            if current.next:
                current.next.prev = None
            self.head = current.next
            current = None
            return

        # Case 2: If the node to be deleted is not the head node
        while current is not None and current.data != key:
            current = current.next

        if current is None:
            print("Data not found in the list.")
            return

        if current.next:
            current.next.prev = current.prev

        if current.prev:
            current.prev.next = current.next

        current = None

    # Method to display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# Main function to demonstrate the doubly linked list operations
if __name__ == "__main__":
    linked_list = DoublyLinkedList()

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
            print("Doubly Linked List:")
            linked_list.display()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
