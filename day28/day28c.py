class TicketBookingSystem:
    def __init__(self, total_tickets):
        self.total_tickets = total_tickets
        self.available_tickets = total_tickets
        self.bookings = {}

    def show_available_tickets(self):
        print(f"\nAvailable Tickets: {self.available_tickets}")

    def book_ticket(self, name, num_tickets):
        if num_tickets <= self.available_tickets:
            self.available_tickets -= num_tickets
            if name in self.bookings:
                self.bookings[name] += num_tickets
            else:
                self.bookings[name] = num_tickets
            print(f"\n{name} successfully booked {num_tickets} ticket(s).")
        else:
            print("\nNot enough tickets available!")

    def cancel_ticket(self, name):
        if name in self.bookings:
            cancelled = self.bookings.pop(name)
            self.available_tickets += cancelled
            print(f"\n{name}'s {cancelled} ticket(s) cancelled.")
        else:
            print("\nNo booking found for this name.")

    def show_bookings(self):
        print("\nCurrent Bookings:")
        if not self.bookings:
            print("No bookings yet.")
        else:
            for name, tickets in self.bookings.items():
                print(f"{name}: {tickets} ticket(s)")



def main():
    system = TicketBookingSystem(100) 

    while True:
        print("\n--- Ticket Booking System ---")
        print("1. Show Available Tickets")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. Show Bookings")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            system.show_available_tickets()

        elif choice == '2':
            name = input("Enter your name: ")
            num = int(input("Enter number of tickets: "))
            system.book_ticket(name, num)

        elif choice == '3':
            name = input("Enter your name: ")
            system.cancel_ticket(name)

        elif choice == '4':
            system.show_bookings()

        elif choice == '5':
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()