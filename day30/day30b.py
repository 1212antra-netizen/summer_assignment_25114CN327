books = []
issued = []

while True:
    print("\n===== MINI LIBRARY SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        books.append(book)
        print("Book added successfully!")

    elif choice == 2:
        if len(books) == 0:
            print("No books available.")
        else:
            print("\nAvailable Books:")
            for b in books:
                print(b)

    elif choice == 3:
        name = input("Enter book name to search: ")
        if name in books:
            print("Book is available.")
        else:
            print("Book not found.")

    elif choice == 4:
        name = input("Enter book name to issue: ")
        if name in books:
            books.remove(name)
            issued.append(name)
            print("Book issued successfully!")
        else:
            print("Book not available.")

    elif choice == 5:
        name = input("Enter book name to return: ")
        if name in issued:
            issued.remove(name)
            books.append(name)
            print("Book returned successfully!")
        else:
            print("Invalid return.")

    elif choice == 6:
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice. Try again.")