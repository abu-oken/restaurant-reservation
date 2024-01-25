class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, description):
        self.items[name] = {'price': price, 'description': description}

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def update_item(self, name, price, description):
        if name in self.items:
            self.items[name] = {'price': price, 'description': description}

    def search(self, keyword):
        results = [item for item in self.items.keys() if keyword.lower() in item.lower()]
        return results

    def print_menu(self):
        for name, details in self.items.items():
            print(f"{name}: ${details['price']} - {details['description']}")

class Reservation:
    def __init__(self, customer_name, date, time, num_guests, menu):
        self.customer_name = customer_name
        self.date = date
        self.time = time
        self.num_guests = num_guests
        self.menu = menu
        self.meals = {}

    def add_meal(self, meal_name):
        if meal_name in self.menu.items and len(self.meals) < 10:
            self.meals[meal_name] = self.menu.items[meal_name]

    def remove_meal(self, meal_name):
        if meal_name in self.meals:
            del self.meals[meal_name]

    def calculate_total(self):
        return sum(meal['price'] for meal in self.meals.values())

    def __str__(self):
        reservation_details = f"Reservation for {self.customer_name} on {self.date} at {self.time} for {self.num_guests} guests"
        meal_details = "\n".join([f"{meal}: ${details['price']:.2f}" for meal, details in self.meals.items()])
        total_price = f"Total: ${self.calculate_total():.2f}"
        return f"{reservation_details}\n{meal_details}\n{total_price}"

class ReservationManager:
    def __init__(self):
        self.reservations = {}

    def create_reservation(self, reservation_id, customer_name, date, time, num_guests, menu):
        if reservation_id not in self.reservations:
            reservation = Reservation(customer_name, date, time, num_guests, menu)
            self.reservations[reservation_id] = reservation

    def update_reservation(self, reservation_id, **kwargs):
        if reservation_id in self.reservations:
            reservation = self.reservations[reservation_id]
            for key, value in kwargs.items():
                setattr(reservation, key, value)

    def delete_reservation(self, reservation_id):
        if reservation_id in self.reservations:
            del self.reservations[reservation_id]

    def view_reservation(self, reservation_id=None):
        if reservation_id is not None:
            print(self.reservations.get(reservation_id, "Reservation not found."))
        else:
            for reservation_id, reservation in self.reservations.items():
                print(f"Reservation ID: {reservation_id}")
                print(reservation)
                print()

    def search_reservations(self, customer_name):
        results = [reservation_id for reservation_id, reservation in self.reservations.items() if
                customer_name.lower() in reservation.customer_name.lower()]
        return results

class Staff:
    def __init__(self, menu):
        self.menu = menu
        self.reservations = []

    def view_menu(self):
        self.menu.print_menu()

    def view_restaurant_details(self):
        # Add restaurant details here
        print("Restaurant Details:")
        print("Name: Asude")
        print("Address: Hallaxona")
        print("Phone Number: +998908169694")
        print("Website: www.asude.com")
        print("Opening Hours: Mon-Sun 8:00 AM - 11:00 PM")

    def view_all_reservations(self):
        for reservation in self.reservations:
            print(reservation)

    def view_reservation_details(self, customer_name):
        matching_reservations = [
            res for res in self.reservations
            if res.customer_name.lower() == customer_name.lower()
        ]

        for reservation in matching_reservations:
            print(reservation)

    def update_reservation_details(self, customer_name, new_date, new_time, new_num_guests):
        matching_reservations = [
            res for res in self.reservations
            if res.customer_name.lower() == customer_name.lower()
        ]

        for reservation in matching_reservations:
            reservation.date = new_date
            reservation.time = new_time
            reservation.num_guests = new_num_guests

        print(f"Reservation details updated for {customer_name}.")

    def cancel_reservation(self, customer_name):
        matching_reservations = [
            res for res in self.reservations
            if res.customer_name.lower() == customer_name.lower()
        ]

        if matching_reservations:
            self.reservations.remove(matching_reservations[0])
            print(f"Reservation canceled for {customer_name}.")
        else:
            print(f"No reservation found for {customer_name}.")

    def add_new_menu_item(self, name, price):
        self.menu.add_item(name, price)
        print(f"New menu item '{name}' added.")

    def update_menu_item(self, name, new_price):
        if name in self.menu.items:
            self.menu.items[name] = new_price
            print(f"Menu item '{name}' updated with new price: ${new_price:.2f}.")
        else:
            print(f"No menu item found with the name '{name}'.")

    def delete_menu_item(self, name):
        if name in self.menu.items:
            del self.menu.items[name]
            print(f"Menu item '{name}' deleted.")
        else:
            print(f"No menu item found with the name '{name}'.")

def main():

    menu = Menu()
    menu.add_item("osh", 25.00, "Choyxona osh")
    menu.add_item("Norin", 20.00, "Dunyo reytingidagi top norin")
    menu.add_item("Somsa", 5.00, "Izlab topomagan somsez")
    menu.add_item("Shorva", 15.00, "Xayotizni ozgartirvoradigan shorva")
    menu.add_item("Qozonkabob", 30.00, "Donald Trump maqtagan qazonkabob")
    menu.add_item("Tovuq", 15.00, "Yesez paqillab yurasiz")
    menu.add_item("Choy", 3.00, "")
    menu.add_item("Non", 4.00, "")

    reservation_manager = ReservationManager()
    staff = Staff(menu)

    while True:
        print("\n===== Restaurant System =====")
        print("1. Customer")
        print("2. Staff")
        print("3. Exit")

        user_type = input("Enter your user type (1-3): ")

        if user_type == "1":
            # Customer
            print("\n===== Restaurant Reservation System =====")
            print("1. Make a Reservation")
            print("2. Update Reservation")
            print("3. Cancel Reservation")
            print("4. View Reservation")
            print("5. Search Reservations")
            print("6. Display Menu")
            print("7. Exit")

            choice = input("Enter your choice (1-7): ")

            if choice == "1":
                customer_name = input("Enter customer name: ")
                date = input("Enter reservation date (YYYY-MM-DD): ")
                time = input("Enter reservation time (HH:MM): ")
                num_guests = int(input("Enter number of guests: "))

                print("Menu:")
                menu.print_menu()

                reservation_id = len(reservation_manager.reservations) + 1
                reservation_manager.    create_reservation(reservation_id, customer_name, date, time, num_guests, menu)

                meal_choice = input("Enter meal choice (type 'done' to finish): ")
                while meal_choice.lower() != 'done':
                    reservation_manager.reservations[reservation_id].add_meal(meal_choice)
                    meal_choice = input("Enter another meal choice (type 'done' to finish): ")

                print("Reservation successfully created!")

            elif choice == "2":
                reservation_id = int(input("Enter reservation ID to update: "))
                reservation_manager.view_reservation(reservation_id)

                field = input("Enter field to update (customer_name, date, time, num_guests): ")
                value = input(f"Enter new value for {field}: ")

                if field == "num_guests":
                    value = int(value)

                reservation_manager.update_reservation(reservation_id, **{field: value})
                print("Reservation successfully updated!")

            elif choice == "3":
                reservation_id = int(input("Enter reservation ID to cancel: "))
                reservation_manager.delete_reservation(reservation_id)
                print("Reservation successfully canceled!")

            elif choice == "4":
                reservation_id = int(input("Enter reservation ID to view (enter 0 to view all): "))
                reservation_manager.view_reservation(reservation_id)

            elif choice == "5":
                customer_name = input("Enter customer name to search: ")
                results = reservation_manager.search_reservations(customer_name)

                if results:
                    print(f"Found {len(results)} reservations:")
                    for result in results:
                        reservation_manager.view_reservation(result)
                else:
                    print("No reservations found for the given customer.")

            elif choice == "6":
                print("Menu:")
                menu.print_menu()

            elif choice == "7":
                print("Exiting Restaurant Reservation System. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 7.")


        elif user_type == "2":
            # Staff
            staff_options = {
                "1": staff.view_menu,
                "2": staff.view_restaurant_details,
                "3": staff.view_all_reservations,
                "4": lambda: staff.view_reservation_details(input("Enter customer name: ")),
                "5": lambda: staff.update_reservation_details(
                    input("Enter customer name: "),
                    input("Enter new date (YYYY-MM-DD): "),
                    input("Enter new time (HH:MM): "),
                    int(input("Enter new number of guests: "))
                ),
                "6": lambda: staff.cancel_reservation(input("Enter customer name: ")),
                "7": lambda: staff.add_new_menu_item(
                    input("Enter menu item name: "),
                    float(input("Enter menu item price: "))
                ),
                "8": lambda: staff.update_menu_item(
                    input("Enter menu item name to update: "),
                    float(input("Enter new price: "))
                ),
                "9": lambda: staff.delete_menu_item(input("Enter menu item name to delete: ")),
            }

            while True:
                print("\n===== Staff Options =====")
                print("1. View Menu")
                print("2. View Restaurant Details")
                print("3. View All Reservations")
                print("4. View Reservation Details for a Customer")
                print("5. Update Reservation Details for a Customer")
                print("6. Cancel Reservation for a Customer")
                print("7. Add New Menu Item")
                print("8. Update Menu Item")
                print("9. Delete Menu Item")
                print("10. Back")

                staff_choice = input("Enter your choice (1-10): ")

                if staff_choice == "10":
                    break
                elif staff_choice in staff_options:
                    staff_options[staff_choice]()
                else:
                    print("Invalid choice. Please enter a number between 1 and 10.")

        elif user_type == "3":
            # Exit
            print("Exiting Restaurant System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
