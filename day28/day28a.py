class Book:
    def __init__(self, bid, title, author):
        self.bid = bid
        self.title = title
        self.author = author
        self.issued = False

    def display(self):
        status = "Issued" if self.issued else "Available"
        print(f"{self.bid}\t{self.title}\t{self.author}\t{status}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        print("\n--- Add Book ---")
        bid = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")

        self.books.append(Book(bid, title, author))
        print("Book added!")
        input("Press Enter to continue...")

    def view_books(self):
        print("\n--- Book List ---")
        if not self.books:
            print("No books available.")
        else:
            print("ID\tTitle\tAuthor\tStatus")
            for book in self.books:
                book.display()
        input("\nPress Enter to continue...")

    def issue_book(self):
        bid = input("\nEnter Book ID to issue: ")
        for book in self.books:
            if book.bid == bid:
                if not book.issued:
                    book.issued = True
                    print("✅ Book issued successfully!")
                else:
                    print("❌ Book already issued.")
                break
        else:
            print("Book not found.")
        input("\nPress Enter to continue...")

    def return_book(self):
        bid = input("\nEnter Book ID to return: ")
        for book in self.books:
            if book.bid == bid:
                if book.issued:
                    book.issued = False
                    print("✅ Book returned successfully!")
                else:
                    print("❌ Book was not issued.")
                break
        else:
            print("Book not found.")
        input("\nPress Enter to continue...")

    def search_book(self):
        title = input("\nEnter Book Title to search: ").lower()
        found = False
        for book in self.books:
            if title in book.title.lower():
                book.display()
                found = True
        if not found:
            print("No matching book found.")
        input("\nPress Enter to continue...")



lib = Library()

while True:
    print("====== LIBRARY MANAGEMENT SYSTEM ======")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")
    print("=======================================")

    choice = input("Enter your choice: ")

    if choice == '1':
        lib.add_book()
    elif choice == '2':
        lib.view_books()
    elif choice == '3':
        lib.issue_book()
    elif choice == '4':
        lib.return_book()
    elif choice == '5':
        
        lib.search_book()
    elif choice == '6':
        print(" Exiting program...")
        break
    else:
        print("Invalid choice!")
        input("Press Enter to continue...")