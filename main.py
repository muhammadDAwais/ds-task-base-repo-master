# main.py

# This file contains a menu-driven application to perform basic data structure operations.
# Students are expected to implement missing features or enhance existing ones.

def add_integers(a, b):
    return a + b

# Example usage:
result = add_integers(5, 3)
print("The sum is:", result)


def display_menu():
    print("\nData Structure Task App")
    print("1. Stack Operations")
    print("2. Queue Operations")
    print("3. Dictionary Operations")
    print("4. Exit")

def stack_operations():
    stack = []
    print("\n-- Stack Operations --")
    while True:
        print("1. Push\n2. Pop\n3. Display\n4. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            item = input("Enter item to push: ")
            stack.append(item)
        elif choice == "2":
            if stack:
                print("Popped item:", stack.pop())
            else:
                print("Stack is empty.")
        elif choice == "3":
            print("Stack content:", stack)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

def queue_operations():
    # TODO: Implement queue using list or collections.deque
    print("\n-- Queue Operations --")
    print("TODO: Implement this feature")

def dictionary_operations():
    # TODO: Implement basic dictionary operations like add, delete, search, display
    print("\n-- Dictionary Operations --")
    print("TODO: Implement this feature")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            stack_operations()
        elif choice == "2":
            queue_operations()
        elif choice == "3":
            dictionary_operations()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
