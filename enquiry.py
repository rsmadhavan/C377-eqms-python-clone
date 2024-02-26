import source
import product1

enquiries = []

def display_source():
    source.display_source()

def get_source():
    return source.get_source()

def str_to_dict(string):
    stripped_string = string.strip('{}')
 
    pairs = stripped_string.split(', ')
 
    return {key[1:-1]: value[1:-1] for key, value in (pair.split(': ') for pair in pairs)}
 
def read_data():
    with open('enquiry.txt','r') as file:
        data=file.readlines()
        list_dict=[]
        for line in data:
            temp_dict=str_to_dict(line)
            list_dict.append(temp_dict)
        return list_dict

def display_enquiries():
    enquiries=read_data()
    print("E.no\tName\tDate\tContact Person  Address\tPhone number\tEmail    \tSource\tProduct enquired")
    for enquiry_dict in enquiries:
        row=''
        for value in enquiry_dict.values():
            row+=f'{value}\t'
        print(row)

def add_enquiry():
    enquiry_number = input("Enter enquiry number: ")
    customer_name = input("Enter customer name: ")
    date = input("Enter date: ")
    contact_person = input("Enter contact person: ")
    address = input("Enter address: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    display_source()
    list_source=get_source()
    source_option=int(input("Enter source choice: ")) - 1
    source = list_source[source_option] if source_option in range(len(list_source)) else 'default'
    product_enquired = input("Enter product enquired: ")

    global enquiries
    if not enquiries:
        enquiries=read_data()    

    enquiries.append({
        "Enquiry Number": enquiry_number,
        "Customer Name": customer_name,
        "Date": date,
        "Contact Person": contact_person,
        "Address": address,
        "Phone Number": phone_number,
        "Email": email,
        "Source": source,
        "Product enquired": product_enquired
    })
    save_data()
    print("enquiry added successfully.")

def delete_enquiry(enquiry_number):
    global enquiries
    if not enquiries:
        enquiries=read_data()
 
    for enquiry in enquiries:
        if enquiry["Enquiry Number"] == enquiry_number:
            enquiries.remove(enquiry)
            break  
    save_data()
    print("enquiry deleted successfully.")

# Searchin functionatily is broken
# update logic to search using the key or just revert to list
def search_enquiry(enquiry_number):
    global enquiries
    if not enquiries:
        enquiries=read_data()
    found = False
    for dict in enquiries:
        if dict['Enquiry Number']==str(enquiry_number):
            print(dict)
            found=True
            break
    if not found:
        print("Enquiry not found.")

def save_data():
    file_path = "enquiry.txt"  
    with open(file_path, "w") as f:
        for enquiry in enquiries:
            f.write(str(enquiry) + '\n')
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
            display_enquiries()
        elif choice == "2":
            add_enquiry()
        elif choice == "3":
            enquiry_number = input("Enter enquiry number to delete: ")
            delete_enquiry(enquiry_number)
        elif choice == "4":
            enquiry_number = input("Enter enquiry number to search: ")
            search_enquiry(enquiry_number)
        elif choice == "5":
            print("\n... GOING BACK ...")
            break
        elif choice =="6":
            read_data()
        elif choice=='7':
            test_source()
        else:
            print("Invalid choice. Please try again.")

# Start the main menu
#enquiry_menu()
