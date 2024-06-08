from collections import deque

class Steque:
    def __init__(self):
        self.deque = deque()

    def push(self, element):
        self.deque.appendleft(element)
        print(f"Pushed: {element}")

    def pop(self):
        if self.deque:
            element = self.deque.popleft()
            print(f"Popped: {element}")
            return element
        else:
            print("Steque is empty, cannot pop.")
            return None

    def enqueue(self, element):
        self.deque.append(element)
        print(f"Enqueued: {element}")

    def display(self):
        print(f"Current Steque: {list(self.deque)}")

def main():
    steque = Steque()

    while True:
        user_input = input("Enter 'push <element>', 'pop', 'enqueue <element>', or 'exit' to stop: ").strip()

        if user_input.lower() == 'exit':
            break
        elif user_input.lower().startswith('push '):
            element = user_input[5:].strip()
            steque.push(element)
        elif user_input.lower() == 'pop':
            steque.pop()
        elif user_input.lower().startswith('enqueue '):
            element = user_input[8:].strip()
            steque.enqueue(element)
        else:
            print("Invalid command. Please enter 'push <element>', 'pop', 'enqueue <element>', or 'exit'.")

        steque.display()

    print("Steque processing complete.")

if __name__ == "__main__":
    main()
