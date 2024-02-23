def get_source():
    try:
        with open('source.txt', 'r') as file:
            source=file.readlines()
            source=[s.strip() for s in source]
            return source
    except FileNotFoundError:
        print("Error: Could not find the file 'source.txt'")
        return []

def display_source():
    with open('source.txt', 'r') as file:
        source=file.readlines()
        source=[s.strip() for s in source]
        for i in range(len(source)):
            print(f"{i+1} : {source[i]}")

def add_source():
    source=input("ENTER THE SOURCE : ")
    with open('source.txt', 'a') as file:
        file.write('\n')
        file.write(source)

<<<<<<< HEAD
print(get_source())
=======
def source_menu():
    print(f'''
        SOURCE MENU
        -------------
        1. ADD SOURCE
        2. DISPLAY SOURCE
        3. GO BACK
              ''')
    choice=input("ENTER CHOICE : ")
    if choice=='1':
        add_source()
    elif choice=='2':
        display_source()
    else:
        print("... GOING BACK ...")
>>>>>>> b22d2f41088bcdffea6ffe92ce8e27990661a32c
