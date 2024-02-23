#import enquiry
#import product
import source

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. PRODUCT MENU")
        print("2. SOURCE MENU")
        print("3. ENQUIRY MENU")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            pass
            #product.product_menu()
        elif choice == "2":
            source.source_menu()
        elif choice == "3":
            pass
            #enquiry.main_menu()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()