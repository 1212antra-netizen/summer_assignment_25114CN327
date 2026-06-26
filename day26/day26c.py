balance = 10000   
pin = "1234"      

print("🏧 Welcome to ATM")

entered_pin = input("Enter your PIN: ")

if entered_pin == pin:
    while True:
        print("\nChoose an option:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            print("Your balance is:", balance)

        elif choice == "2":
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print("✅Amount deposited successfully")

        elif choice == "3":
            amount = int(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(" Please collect your cash")
            else:
                print(" Insufficient balance")

        elif choice == "4":
            print(" Thank you for using ATM")
            break

        else:
            print("Invalid choice")

else:
    print("Wrong PIN")