def display(s):
    print("Current string:", s)
    input("Press Enter to continue...")


def length(s):
    print("Length of string:", len(s))
    input("Press Enter to continue...")


def concatenate(s):
    s2 = input("Enter another string: ")
    result = s + s2
    print("Concatenated string:", result)
    input("Press Enter to continue...")
    return result


def reverse(s):
    print("Reversed string:", s[::-1])
    input("Press Enter to continue...")


def compare(s):
    s2 = input("Enter another string: ")
    if s == s2:
        print("Strings are equal.")
    else:
        print("Strings are not equal.")
    input("Press Enter to continue...")


def to_upper(s):
    print("Uppercase string:", s.upper())
    input("Press Enter to continue...")


def to_lower(s):
    print("Lowercase string:", s.lower())
    input("Press Enter to continue...")


# Main Program
s = ""

while True:
    print("\n--- String Operations Menu ---")
    print("1. Enter String")
    print("2. Display String")
    print("3. Find Length")
    print("4. Concatenate String")
    print("5. Reverse String")
    print("6. Compare Strings")
    print("7. Convert to Uppercase")
    print("8. Convert to Lowercase")
    print("9. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        s = input("Enter a string: ")
        input("Press Enter to continue...")

    elif choice == 2:
        display(s)

    elif choice == 3:
        length(s)

    elif choice == 4:
        s = concatenate(s)

    elif choice == 5:
        reverse(s)

    elif choice == 6:
        compare(s)

    elif choice == 7:
        to_upper(s)

    elif choice == 8:
        to_lower(s)

    elif choice == 9:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
        input("Press Enter to continue...")