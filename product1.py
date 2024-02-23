def add_product(new_product_data):
    with open('product.txt', 'a') as file:
        file.write(new_product_data + '\n')

#new_product_data = ['laptop',5, 65000, 'New laptop']
#add_product(new_product_data)

def display_product():
    try:
        with open('product.txt', 'r') as file:
            products=file.readlines()
            product=[p.strip() for p in products]
            for i in range(len(products)):
                print(f"\t{i+1} : {product[i]}")
    except FileNotFoundError:
        print("ERROR : COULD NOT FIND THE FILE 'source.txt'")
        return []   

def get_product():
    try:
        with open('product.txt', 'r') as file:
            products=file.readlines()
            product=[p.strip() for p in products]
            return product
    except FileNotFoundError:
        print("ERROR : COULD NOT FIND THE FILE 'source.txt'")
        return []   
#get_product()

def product_menu():
    while True:
        print(f'''
            PRODUCT MENU
            -------------
            1. ADD PRODUCT
            2. DISPLAY PRODUCTS
            3. GO BACK
                ''')
        choice=input("\tENTER CHOICE : ")
        if choice=='1':
            add_product()
        elif choice=='2':
            display_product()
        else:
            print("\n... GOING BACK ...")
            break

#display_product()