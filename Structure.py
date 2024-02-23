
product_items = []
customers = []
employee_details = []


def display_product_items():
    print("Product Items:")
    for product in product_items:
        print(product)


def display_customers():
    print("Customers:")
    for customer in customers:
        print(customer)


def display_employee_details():
    print("Employee Details:")
    for employee in employee_details:
        print(employee)

def add_product_item():
    product_id = input("Enter product ID: ")
    product_name = input("Enter product name: ")
    product_price = input("Enter product price: ")
    product_category = input("Enter product category: ")
    product_description = input("Enter product description: ")
    product_items.append([product_id, product_name, product_price, product_category, product_description])
    save_data()
    print("Product item added successfully.")


def add_customer():
    customer_name = input("Enter customer name: ")
    email = input("Enter email: ")
    phone_number = input("Enter phone number: ")
    address = input("Enter address: ")
    source = input("Enter source: ")
    remark = input("Enter remark: ")
    customers.append([customer_name, email, phone_number, address, source, remark])
    save_data()
    print("Customer added successfully.")

def add_employee():
    name = input("Enter employee name: ")
    rating = input("Enter employee rating: ")
    mobile_number = input("Enter employee mobile number: ")
    employee_details.append([name, rating, mobile_number])
    save_data()
    print("Employee added successfully.")


def save_data():
    file_path = "D:\\data.txt"  
    with open(file_path, "w") as f:
        f.write("Product Items:\n")
        for item in product_items:
            f.write(",".join(item) + '\n')
        f.write("\nCustomers:\n")
        for customer in customers:
            f.write(",".join(customer) + '\n')
        f.write("\nEmployee Details:\n")
        for employee in employee_details:
            f.write(",".join(employee) + '\n')
    print("Data saved successfully.")


def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Product Items")
        print("2. Customers")
        print("3. Employee Details")
        print("4. Add Product Item")
        print("5. Add Customer")
        print("6. Add Employee")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_product_items()
        elif choice == "2":
            display_customers()
        elif choice == "3":
            display_employee_details()
        elif choice == "4":
            add_product_item()
        elif choice == "5":
            add_customer()
        elif choice == "6":
            add_employee()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

# Start the main menu
main_menu()
