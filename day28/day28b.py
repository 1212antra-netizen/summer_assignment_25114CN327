import os

class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("✅ Amount Deposited Successfully!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient Balance!")
        else:
            self.balance -= amount
            print("✅ Withdrawal Successful!")

    def display(self):
        print(f"{self.acc_no}\t{self.name}\t{self.balance}")


class BankSystem:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        print("\n--- Create Account ---")
        acc_no = input("Enter Account Number: ")
        name = input("Enter Name: ")
        balance = float(input("Enter Initial Balance: "))

        self.accounts.append(BankAccount(acc_no, name, balance))
        print("✅ Account Created!")
        input("Press Enter to continue...")

    def view_accounts(self):
        print("\n--- Account List ---")
        if not self.accounts:
            print("No accounts found.")
        else:
            print("AccNo\tName\tBalance")
            print("-" * 30)
            for acc in self.accounts:
                acc.display()
        input("\nPress Enter to continue...")

    def deposit_money(self):
        acc_no = input("\nEnter Account Number: ")
        for acc in self.accounts:
            if acc.acc_no == acc_no:
                amount = float(input("Enter amount to deposit: "))
                acc.deposit(amount)
                break
        else:
            print("Account not found.")
        input("\nPress Enter to continue...")

    def withdraw_money(self):
        acc_no = input("\nEnter Account Number: ")
        for acc in self.accounts:
            if acc.acc_no == acc_no:
                amount = float(input("Enter amount to withdraw: "))
                acc.withdraw(amount)
                break
        else:
            print("Account not found.")
        input("\nPress Enter to continue...")

    def search_account(self):
        acc_no = input("\nEnter Account Number: ")
        for acc in self.accounts:
            if acc.acc_no == acc_no:
                print("\nAccount Found:")
                acc.display()
                break
        else:
            print("Account not found.")
        input("\nPress Enter to continue...")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Main Program
bank = BankSystem()

while True:
    clear_screen()
    print("====== BANK MANAGEMENT SYSTEM ======")
    print("1. Create Account")
    print("2. View Accounts")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Search Account")
    print("6. Exit")
    print("===================================")

    choice = input("Enter your choice: ")

    if choice == '1':
        clear_screen()
        bank.create_account()
    elif choice == '2':
        clear_screen()
        bank.view_accounts()
    elif choice == '3':
        clear_screen()
        bank.deposit_money()
    elif choice == '4':
        clear_screen()
        bank.withdraw_money()
    elif choice == '5':
        clear_screen()
        bank.search_account()
    elif choice == '6':
        print(" Exiting program...")
        break
    else:
        print("Invalid choice!")
        input("Press Enter to continue...")