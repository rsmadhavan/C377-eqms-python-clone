def add_product():
    product_data=[]
    try:
        with open('product.txt', 'a') as file:
            product_data.append(int(input("\t\tENTER CODE:")))
            product_data.append(input("\t\tENTER NAME:"))
            product_data.append(float(input("\t\tENTER PRICE:")))
            product_data.append(input("\t\tENTER DESCRIPTION:"))
            print(product_data)
            file.write('\n')
            file.write(str(product_data))
        print("!!!! SOURCE ADDED SUCCESSFULLY !!!!\n") 
    except Exception as e:
        print(f"ERROR: {e}")
#new_product_data = ['laptop',5, 65000, 'New laptop']
#add_product(new_product_data)

def display_product():
    try:
        with open('product.txt', 'r') as file:
            products=file.readlines()
            product=[p.strip() for p in products]
            print("\t\tNO    : CODE\tPRODUCT NAME\tPRICE\tDESCRIPTION")
            for i in range(len(products)):
                productf=''
                for p in product[i][1:-1].split(','):
                    productf+=f'{p.strip()}\t'
                print(f"\t\tPROD{i+1} : {productf}")
    except FileNotFoundError:
        print("ERROR : COULD NOT FIND THE FILE 'source.txt'")
        return []   

def get_product():
    try:
        with open('product.txt', 'r') as file:
            products=file.readlines()
            product=[p.strip() for p in products]
            return product.strip('[]').split(',')
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
        choice=input("\t\tENTER CHOICE : ")
        if choice=='1':
            add_product()
        elif choice=='2':
            display_product()
        else:
            print("\n... GOING BACK ...")
            break

#display_product()