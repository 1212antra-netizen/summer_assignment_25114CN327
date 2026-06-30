inventory = {}
def add_item():
    name = input("Enter item name: ")
    qty = int(input("Enter quantity: "))
    
    if name in inventory:
        inventory[name] += qty
    else:
        inventory[name] = qty
    
    print("Item added/updated successfully.")
    input("Press Enter to continue...")


def remove_item():
    name = input("Enter item name to remove: ")
    
    if name in inventory:
        del inventory[name]
        print("Item removed successfully.")
    else:
        print("Item not found.")
    
    input("Press Enter to continue...")


def update_item():
    name = input("Enter item name to update: ")
    
    if name in inventory:
        qty = int(input("Enter new quantity: "))
        inventory[name] = qty
        print("Item updated successfully.")
    else:
        print("Item not found.")
    
    input("Press Enter to continue...")


def search_item():
    name = input("Enter item name to search: ")
    
    if name in inventory:
        print(f"{name} → Quantity: {inventory[name]}")
    else:
        print("Item not found.")
    
    input("Press Enter to continue...")


def display_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\n--- Inventory List ---")
        for item, qty in inventory.items():
            print(f"{item} : {qty}")
    
    input("Press Enter to continue...")

while True:
    print("\n--- Inventory Management System ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Update Item Quantity")
    print("4. Search Item")
    print("5. Display Inventory")
    print("6. Exit")
    
    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Invalid input.")
        continue

    if choice == 1:
        add_item()
    elif choice == 2:
        remove_item()
    elif choice == 3:
        update_item()
    elif choice == 4:
        search_item()
    elif choice == 5:
        display_inventory()
    elif choice == 6:
        print("Exiting program...")
        break
    else:
        print("Invalid choice.")
        input("Press Enter to continue...")