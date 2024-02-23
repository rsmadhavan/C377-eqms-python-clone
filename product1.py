def add_product(new_product_data):
    with open('product.txt', 'a') as file:
        file.write(new_product_data + '\n')

new_product_data = ['laptop',5, 65000, 'New laptop']
add_product(new_product_data)


def get_product_data():
    with open('product.txt', 'r') as file:
        products = file.readlines()
        for product in products:
            print(product.strip())
get_product_data()