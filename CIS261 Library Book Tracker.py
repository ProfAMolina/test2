#CIS261
#Santana Howard
#Week 5 Library Book Tracker

from datetime import datetime, timedelta

class Checkout:
    def __init__(self, title, borrower, days, condition, checkout_date_str=None):
        self.title = title
        self.borrower = borrower
        self.days = days
        self.condition = condition
        if checkout_date_str is None:
            self.return_date = datetime.now()
            self.checkout_date = self.return_date - timedelta(days = days)
        else:
            self.checkout_date = datetime.strptime(checkout_date_str, "%Y-%m-%d")
            self.return_date = self.checkout_date - timedelta(days = 14)
        self.due_date = self.checkout_date + timedelta(days = 14)
        self.late_fee = 0.0
        self.damage_fee = 0.0
        self.total_fee = 0.0
        self.calculate_fees()

    def calculate_fees(self):
        if self.days > 14:
            late_days = self.days - 14
            self.late_fee = late_days * 0.25
        if self.condition == "Good":
            self.damage_fee = 0.0
        elif self.condition == "Fair":
            self.damage_fee = 5.0
        elif self.condition == "Damaged":
            self.damage_fee = 15.0
        self.total_fee = self.late_fee + self.damage_fee

    def is_overdue(self):
        return self.days > 14

    def is_damaged(self):
        return self.condition == "Fair" or self.condition == "Damaged"

    def to_file_string(self):
        checkout_date_str = self.checkout_date.strftime("%Y/%m/%d")
        return f"{self.title}|{self.days}|{self.condition}|{self.total_fee:.2f}|{checkout_date_str}"

    def __str__(self):
        checkout_str = self.checkout_date.strftime("%m/%d/%Y")
        due_str = self.due_date.strftime("%m/%d/%Y")
        return_str = self.return_date.strftime("%m/%d/%Y")
        return (f"Book: {self.title}\n"
                f"Borrower: {self.borrower}\n"
                f"Checkout Date: {checkout_str}\n"
                f"Due Date: {due_str}\n"
                f"Return Date: {return_str}\n"
                f"Days Borrowed: {self.days}\n"
                f"Condition: {self.condition}\n"
                f"Fee: ${self.total_fee:.2f}")

class LibrarianUser:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
    
def create_default_users():
    users = []
    admin = LibrarianUser("admin", "library2024", "Admin")
    users.append(admin)
    staff = LibrarianUser("staff", "book123", "Staff")
    users.append(staff)
    return users

def display_login_screen():
    print("\n" + "=" * 50)
    print("LIBRARY BOOK TRACKER - SECURE LOGIN")
    print("=" * 50)
    print("Please log in to continue.")
    print("=" * 50 + "\n")

def authenticate_user(users, username, password):
    for user in users:
        if user.username == username and user.password == password:
            return user
    return None

def display_access_granted(username, role):
    print("\n" + "=" * 50)
    print ("ACCESS GRANTED")
    print("=" * 50)
    print(f"Welcome, {username}!")
    print(f"Your Role: {role}")
    if role == "Admin":
        print("\nFull Access: Process retunrs + Generate Report")
    else:
        print("\nRead-Only Access: Generate reports only")
    print("=" * 50)
    input("\nPress Enter to continue...")

def display_access_denied():
    print("\n" + "=" * 50)
    print("ACCESS DENIED")
    print("=" * 50)
    print("Invalid username or password.")
    print("\n" + "=" * 50 + "\n")

def display_menu(role):
    print("\n" + "=" * 50)
    print(f"MAIN MENU - {role} Access")
    print("=" * 50)
    if role == "Admin":
        print("1. Process Book Returns")
        print("2. Generate Reports")
        print("3. Exit")
    else:
        print("1. Generate Reports")
        print("2. Exit")
    print("=" * 50)

def get_menu_choice():
    return input("Enter your choice: ")

def display_all_checkouts(checkouts):
    print("=" * 50)
    print("All Book Checkouts - Detailed Lists")
    print("=" * 50)
    for i, checkout in enumerate(checkouts, 1):
        checkout_str = checkout.checkout_date.strftime("%m/%d/%Y")
        due_str = checkout.due_date.strftime("%m/%d/%Y")
        return_str = checkout.return_date.strftime("%m/%d/%Y")
        print(f"\nCheckout #{i + 1}:")
        print(f" Checkout Date: {checkout_str}")
        print(f" Due Date: {due_str}")
        print(f" Return Date: {return_str}")
        print(f" Book: {checkout.title}")
        print(f" Borrower: {checkout.borrower}")
        print(f" Days Borrowed: {checkout.days}")
        print(f" Condition: {checkout.condition}")
        print(f" Late Fee: ${checkout.late_fee:.2f}")
        print(f" Damage Fee: ${checkout.damage_fee:.2f}")
        print(f" Total Fee: ${checkout.total_fee:.2f}")
    print("=" * 50)

def calculate_statistics(checkouts):
    if len(checkouts) == 0:
        return 0.0, 0.0, 0.0, 0.0
    fees = [checkout.total_fee for checkout in checkouts]
    total_fees = sum(fees)
    average_fees = total_fees / len(fees)
    highest_fee = max(fees)
    lowest_fee = min(fees)
    return total_fees, average_fees, highest_fee, lowest_fee

def find_checkouts_by_borrower(checkouts, borrower_name):
    results = []
    for checkout in checkouts:
        if checkout.borrower.lower() == borrower_name.lower():
            results.append(checkout)
    return results

def find_overdue_books(checkouts):
    overdue = []
    for checkout in checkouts:
        if checkout.is_overdue():
            overdue.append(checkout)
    return overdue

def find_damaged_books(checkouts):
    damaged = []
    for checkout in (checkouts):
        if checkout.is_damaged():
            damaged.append(checkout)
    return damaged

def display_filtered_checkouts(checkouts, filter_description):
    print("\n" + "=" * 50)
    print(f"{filter_description.upper()}")
    print("=" * 50)
    if len(checkouts) == 0:
        print("No matching record found.")
    else:
        print(f"Found {len(checkouts)} record(s):\n")
        for checkout in checkouts:
            return_str = checkout.return_date.strftime("%m/%d/%Y")
            print(f"Book: {checkout.title}")
            print(f" Date: {return_str}")
            print(f" Borrower: {checkout.borrower}")
            print(f" Days: {checkout.days}, Condition: {checkout.condition}")
            print(f" Fee: ${checkout.total_fee:.2f}")
            print()
            print("=" * 50)

def generate_report(checkouts):
    today = datetime.now().strftime("%m/%d/%Y")
    print("\n" + "=" * 50)
    print(" LIBRARY BOOK TRACKER - COMPLETE REPORT")
    print(f" Report Date: {today}")
    print("=" * 50)
    if len(checkouts) == 0:
        print("No records to display.")
        print("=" * 50)
        return
    print(f"\nTotal Checkouts in System: {len(checkouts)}")
    print("\n---All Checkouts---")
    for i, checkout in enumerate(checkouts, 1):
        checkout_str = checkout.checkout_date.strftime("%m/%d/%Y")
        due_str = checkout.due_date.strftime("%m/%d/%Y")
        return_str = checkout.return_date.strftime("%m/%d/%Y")
        print(f"\n{i}. {checkout.title} - {checkout.borrower}")
        print(f"Checked Out: {checkout_str} | Due: {due_str} | Returned: {return_str}")
        print(f"Days: {checkout.days}, Condition: {checkout.condition} Fee: ${checkout.total_fee:.2f}")

    fees = [c.total_fee for c in checkouts]
    total_fees = sum(fees)
    average_fee = total_fees / len(fees)
    overdue_count = sum(1 for c in checkouts if c.is_overdue())
    damaged_count = sum(1 for c in checkouts if c.is_damaged())

    print("\n---Statistics---")
    print(f"Total Fee Collected: ${total_fees:.2f}")
    print(f"Average Fee per Checkout: ${average_fee:.2f}")
    print(f"Overdue Returns: {overdue_count}")
    print(f"Damaged Books: {damaged_count}")
    print("\n" + "+" * 50)
    input("Press Enter to return to menu...")
    
def save_checkouts_to_file(checkouts, filename):
    try:
        with open(filename, 'a') as file:
            for checkout in checkouts:
                line = checkout.to_file_string()
                file.write(line + "\n")
        print("\n" + "=" * 50)
        print("FILE SAVE SUCCESSFUL")
        print("=" * 50)
        print(f"Saved {len(checkouts)} record(s) to: {filename}")
        print("=" * 50)
    except Exception as e:
        print(f"\nError saving file: {e}")

def load_checkouts_from_file(filename):
    checkouts = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    date_object = datetime.strptime(parts[5], "%Y-%m-%d")
                    checkout = Checkout(
                    title=parts[0],
                    borrower=parts[1],
                    days=int(parts[2]),
                    condition=parts[3],
                    checkout_date_str=parts[4]
                    )
                    checkouts.append(checkout)
        print(f"Loaded {len(checkouts)} record(s) from{filename}")
    except FileNotFoundError:
        print(f"No previous data found in {filename}")
    except Exception as e:
        print(f"Error reading file: {e}")
    return checkouts
    
def process_returns(filename):
    print("\n" + "=" * 50)
    print("PROCESS BOOK RETURN")
    print("=" * 50)
    print("Tip: Type 'ESC' when finsihed\n")
    checkouts = []
    while True:
        print("\n--- Enter Book Return Information ---")
        title = input("Book title (or type 'ESC' to finsih): ")
        if title.upper() == "ESC":
            break
        borrower = input("Borrower name: ")
        days = int(input("Days borrowed: "))
        print("Condition options: Good, Fair, Damaged")
        condition = input("Book condition: ")
        checkout = Checkout(title, borrower, days, condition)
        today = datetime.now().strftime("%m/%d/%Y")
        print("\n" + "=" * 50)
        print("CHECKOUT PROCESSED")
        print(f"Date: {today}")
        print("=" * 50)
        print(f"Book Title: {checkout.title}")
        print(f"Borrower: {checkout.borrower}")
        print(f"Days Borrowed: {checkout.days}")
        print(f"Book Condition: {checkout.condition}")
        print(f"Total Fee: ${checkout.total_fee:.2f}")
        print("=" * 50)
        print("Book return recorded successfully!\n")
        checkouts.append(checkout)
    if len(checkouts) > 0:
        save_checkouts_to_file(checkouts, filename)
    else:
        print("\nNo books were processed. ")

def generate_reports(filename):
    print("\n" + "=" * 50)
    print(" GENERATE REPORTS")
    print("=" * 50)
    checkouts = load_checkouts_from_file(filename)
    if len(checkouts) == 0:
        print("\nNo checkout records found in system.")
        print("Press enter to continue...")
        return
    generate_report(checkouts)

def main():
    filename = "checkouts.txt"
    valid_users = create_default_users()
    display_login_screen()
    username = input("Username: ")
    password = input("Password: ")
    current_user = authenticate_user(valid_users, username, password)
    if current_user is None:
        display_access_denied()
        return
    display_access_granted(current_user.username, current_user.role)
    while True:
        display_menu(current_user.role)
        choice = get_menu_choice()
        if choice == "1":
            if current_user.role == "Admin":
                process_returns(filename)
            else:
                generate_reports(filename)
        elif choice == "2":
            if current_user.role == "Admin":
                generate_reports(filename)
            else:
                print(f"\nThank you, {current_user.username}!")
                print("Logging out...")
                break
        elif choice == "3" and current_user.role == "Admin":
            print(f"\nThank you, {current_user.username}!")
            print("Logging out...")
            break
        else:
            print("\nInvalid choice Please try again.")
main()
