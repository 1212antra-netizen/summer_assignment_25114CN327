import os

class ContactManager:
    def __init__(self):
        self.contacts = {}

    # Add contact
    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")

        if name in self.contacts:
            print("Contact already exists!")
        else:
            self.contacts[name] = [phone, email]
            print("Contact added successfully.")

    # View contacts
    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details[0]}, Email: {details[1]}")

    # Search contact
    def search_contact(self):
        name = input("Enter name to search: ")
        if name in self.contacts:
            print(f"Name: {name}, Phone: {self.contacts[name][0]}, Email: {self.contacts[name][1]}")
        else:
            print("Contact not found.")

    # Update contact
    def update_contact(self):
        name = input("Enter name to update: ")
        if name in self.contacts:
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            self.contacts[name] = [phone, email]
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    # Delete contact
    def delete_contact(self):
        name = input("Enter name to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    # Clear screen using os
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')


# Program starts here (no main function)
manager = ContactManager()

while True:
    manager.clear_screen()
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        manager.add_contact()
        input("\nPress Enter to continue...")

    elif choice == '2':
        manager.view_contacts()
        input("\nPress Enter to continue...")

    elif choice == '3':
        manager.search_contact()
        input("\nPress Enter to continue...")

    elif choice == '4':
        manager.update_contact()
        input("\nPress Enter to continue...")

    elif choice == '5':
        manager.delete_contact()
        input("\nPress Enter to continue...")

    elif choice == '6':
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
        input("\nPress Enter to continue...")