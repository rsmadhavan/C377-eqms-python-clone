inquiries = []

def display_inquiries():
    with open('D:\\data.txt', 'r') as file:
        data = file.readlines()
        for line in data:
            print(line.strip())

def add_inquiry():
    inquiry_number = input("Enter inquiry number: ")
    customer_name = input("Enter customer name: ")
    date = input("Enter date: ")
    contact_person = input("Enter contact person: ")
    address = input("Enter address: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    source = input("Enter source: ")
    product_inquired = input("Enter product inquired: ")
    
    inquiries.append({
        "Inquiry Number": inquiry_number,
        "Customer Name": customer_name,
        "Date": date,
        "Contact Person": contact_person,
        "Address": address,
        "Phone Number": phone_number,
        "Email": email,
        "Source": source,
        "Product Inquired": product_inquired
    })
    save_data()
    print("Inquiry added successfully.")

def delete_inquiry(inquiry_number):
    global inquiries
    for inquiry in inquiries:
        if inquiry["Inquiry Number"] == inquiry_number:
            inquiries.remove(inquiry)
            break  
    save_data()
    print("Inquiry deleted successfully.")


def search_inquiry(inquiry_number):
    found = False
    with open('D:\\data.txt', 'r') as file:
        data = file.readlines()
        for line in data:
            if "Inquiry Number" in line and inquiry_number in line:
                print(line.strip())
                found = True
                break
    if not found:
        print("Inquiry not found.")

def save_data():
    file_path = "D:\\data.txt"  
    with open(file_path, "w") as f:
        f.write("Inquiries:\n")
        for inquiry in inquiries:
            f.write(str(inquiry) + '\n')
    print("Data saved successfully.")

def enquiry_menu():
    while True:
        print("""
            ENQUIRY MENU:
            --------------------
            1. DISPLAY ENQUIRIES
            2. ADD ENQUIRY
            3. DELETE ENQUIRY
            4. SEARCH ENQUIRY
            5. GO BACK
            """)
        choice = input("\tEnter your choice: ")
        if choice == "1":
            display_inquiries()
        elif choice == "2":
            add_inquiry()
        elif choice == "3":
            inquiry_number = input("Enter inquiry number to delete: ")
            delete_inquiry(inquiry_number)
        elif choice == "4":
            inquiry_number = input("Enter inquiry number to search: ")
            search_inquiry(inquiry_number)
        elif choice == "5":
            print("\n... GOING BACK ...")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the main menu
#enquiry_menu()
