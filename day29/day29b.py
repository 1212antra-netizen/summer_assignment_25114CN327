def display(arr):
    if len(arr) == 0:
        print("Array is empty.")
    else:
        print("Array elements:", arr)
    input("Press Enter to continue...")


def insert(arr):
    try:
        pos = int(input(f"Enter position (1 to {len(arr)+1}): "))
        value = int(input("Enter value: "))
        
        if pos < 1 or pos > len(arr) + 1:
            print("Invalid position.")
        else:
            arr.insert(pos - 1, value)
            print("Element inserted.")
    except:
        print("Invalid input.")
    input("Press Enter to continue...")


def delete(arr):
    if len(arr) == 0:
        print("Array is empty.")
        input("Press Enter to continue...")
        return
    
    try:
        pos = int(input(f"Enter position to delete (1 to {len(arr)}): "))
        
        if pos < 1 or pos > len(arr):
            print("Invalid position.")
        else:
            arr.pop(pos - 1)
            print("Element deleted.")
    except:
        print("Invalid input.")
    input("Press Enter to continue...")


def search(arr):
    if len(arr) == 0:
        print("Array is empty.")
        input("Press Enter to continue...")
        return
    
    try:
        value = int(input("Enter element to search: "))
        
        for i in range(len(arr)):
            if arr[i] == value:
                print(f"Element found at position {i+1}")
                break
        else:
            print("Element not found.")
    except:
        print("Invalid input.")
    
    input("Press Enter to continue...")


# Main Program
arr = []

while True:
    print("\n--- Array Operations Menu ---")
    print("1. Create Array")
    print("2. Display Array")
    print("3. Insert Element")
    print("4. Delete Element")
    print("5. Search Element")
    print("6. Exit")
    
    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        try:
            n = int(input("Enter number of elements: "))
            arr = []
            for i in range(n):
                val = int(input(f"Enter element {i+1}: "))
                arr.append(val)
        except:
            print("Invalid input while creating array.")
        input("Press Enter to continue...")

    elif choice == 2:
        display(arr)

    elif choice == 3:
        insert(arr)

    elif choice == 4:
        delete(arr)

    elif choice == 5:
        search(arr)

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
        input("Press Enter to continue...")
