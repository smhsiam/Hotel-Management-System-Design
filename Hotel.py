import random
import datetime

# Global List Declaration
customers = []

# Customer Class to Store Data
class Customer:
    def __init__(self, name, phone, address, checkin, checkout, room_type, room_no, cust_id, days, price, rc, payment_done):
        self.name = name
        self.phone = phone
        self.address = address
        self.checkin = checkin
        self.checkout = checkout
        self.room_type = room_type
        self.room_no = room_no
        self.cust_id = cust_id
        self.days = days
        self.price = price
        self.restaurant_charges = rc
        self.payment_done = payment_done


# Home Function
def home():
    print("\n\t\t\tWELCOME TO HOTEL CITY INN\n")
    print("\t1. Booking")
    print("\t2. Rooms Info")
    print("\t3. Room Service (Menu Card)")
    print("\t4. Payment")
    print("\t5. Record")
    print("\t0. Exit")

    choice = int(input("-> "))
    if choice == 1:
        booking()
    elif choice == 2:
        rooms_info()
    elif choice == 3:
        restaurant()
    elif choice == 4:
        payment()
    elif choice == 5:
        record()
    elif choice == 0:
        print("Thank you for visiting Hotel City Inn!")
        exit()
    else:
        print("Invalid choice! Please try again.")
        home()


# Rooms Info
def rooms_info():
    print("\n\t\tROOMS INFO\n")
    print("1. Standard Non-AC - Taka 3500 per day")
    print("2. Standard AC - Taka 4000 per day")
    print("3. 2-Bed Non-AC - Taka 4500 per day")
    print("4. 2-Bed AC - Taka 5000 per day\n")
    input("Press any key to return to the main menu...")
    home()


# Booking Function
def booking():
    print("\n\t\tROOM BOOKING\n")
    name = input("Name: ").strip()
    phone = input("Phone No.: ").strip()
    address = input("Address: ").strip()
    checkin = input("Check-In Date (DD/MM/YYYY): ").strip()
    checkout = input("Check-Out Date (DD/MM/YYYY): ").strip()

    # Date Validation
    try:
        checkin_date = datetime.datetime.strptime(checkin, "%d/%m/%Y")
        checkout_date = datetime.datetime.strptime(checkout, "%d/%m/%Y")
        if checkout_date <= checkin_date:
            print("Check-Out date must be after Check-In date.")
            return booking()
    except ValueError:
        print("Invalid date format! Please enter the date as DD/MM/YYYY.")
        return booking()

    # Calculate Stay Duration
    days = (checkout_date - checkin_date).days

    print("\nRoom Types:")
    print("1. Standard Non-AC - Taka 3500")
    print("2. Standard AC - Taka 4000")
    print("3. 2-Bed Non-AC - Taka 4500")
    print("4. 2-Bed AC - Taka 5000")
    room_type = int(input("Select Room Type (1-4): "))

    room_prices = {1: 3500, 2: 4000, 3: 4500, 4: 5000}
    room_names = {1: "Standard Non-AC", 2: "Standard AC", 3: "2-Bed Non-AC", 4: "2-Bed AC"}

    if room_type not in room_prices:
        print("Invalid room type selected!")
        return booking()

    room_no = random.randint(100, 999)
    cust_id = random.randint(10, 99)
    price = room_prices[room_type] * days

    # Add Customer to List
    new_customer = Customer(name, phone, address, checkin, checkout, room_names[room_type], room_no, cust_id, days, price, 0, False)
    customers.append(new_customer)

    print("\nRoom Booked Successfully!")
    print(f"Customer ID: {cust_id}")
    print(f"Room No: {room_no}")
    input("Press any key to return to the main menu...")
    home()


# Restaurant Function
def restaurant():
    cust_id = int(input("\nEnter Customer ID: "))
    customer = next((c for c in customers if c.cust_id == cust_id), None)

    if not customer:
        print("Invalid Customer ID!")
        return restaurant()

    print("\n\t\tMENU CARD\n")
    menu = {
        1: ("Panta Bhat & Ilish Fry", 250),
        2: ("Chicken Curry", 150),
        3: ("Beef Rezala", 200),
        4: ("Vegetable Khichuri", 120),
        5: ("Shutki Bharta", 100),
        6: ("Paratha & Egg Curry", 80),
        7: ("Biryani (Chicken)", 180),
        8: ("Biryani (Beef)", 200),
        9: ("Chingri Malai Curry", 300),
        10: ("Mishti Doi", 50),
        11: ("Kacchi Biryani", 250),
        12: ("Aloo Bharta & Dal", 70),
        13: ("Fuchka & Chotpoti", 100),
        14: ("Chicken Tehari", 150),
        15: ("Haleem", 120),
        16: ("Shorshe Ilish", 300),
        17: ("Beef Kalabhuna", 220),
        18: ("Roshogolla (2 pieces)", 30),
        19: ("Chanar Payesh", 60),
        20: ("Fried Rice & Chicken", 180),
    }
    for item, details in menu.items():
        print(f"{item}. {details[0]} - Taka {details[1]}")

    total_bill = 0
    while True:
        choice = int(input("\nEnter item number (1 to 20, or 0 to stop): "))
        if choice == 0:
            break
        elif choice in menu:
            total_bill += menu[choice][1]
        else:
            print("Invalid choice! Try again.")

    customer.restaurant_charges += total_bill
    print(f"\nTotal Restaurant Bill: Taka {total_bill}")
    input("Press any key to return to the main menu...")
    home()


# Payment Function
def payment():
    cust_id = int(input("\nEnter Customer ID: "))
    customer = next((c for c in customers if c.cust_id == cust_id), None)

    if not customer:
        print("Invalid Customer ID!")
        return payment()

    if customer.payment_done:
        print("Payment already completed!")
    else:
        total_amount = customer.price + customer.restaurant_charges
        print(f"\nTotal Amount: Taka {total_amount}")
        print("1. Credit/Debit Card\n2. UPI\n3. Cash")
        payment_mode = int(input("Select Payment Mode: "))
        if payment_mode in [1, 2, 3]:
            customer.payment_done = True
            print("Payment Successful!")
        else:
            print("Invalid payment mode!")

    input("Press any key to return to the main menu...")
    home()


# Record Function
def record():
    print("\n\t\tCUSTOMER RECORDS\n")
    for customer in customers:
        print(f"Name: {customer.name}, Phone: {customer.phone}, Room No: {customer.room_no}, Total Payment: {'Paid' if customer.payment_done else 'Pending'}")
    input("Press any key to return to the main menu...")
    home()

# Run Program
home()