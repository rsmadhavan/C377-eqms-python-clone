import enquiry
import product1
import source

def main_menu():
    while True:
        print("\nMAIN MENU :")
        print("1. PRODUCT MENU")
        print("2. SOURCE MENU")
        print("3. ENQUIRY MENU")
        print("4. EXIT")
        choice = input("Enter your choice: ")
        if choice == "1":
            product1.product_menu()
        elif choice == "2":
            source.source_menu()
        elif choice == "3":
            enquiry.enquiry_menu()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()