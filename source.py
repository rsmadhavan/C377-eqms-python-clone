def get_source():
    try:
        with open('source.txt', 'r') as file:
            source=file.readlines()
            source=[s.strip() for s in source]
            return source
    except FileNotFoundError:
        print("ERROR : COULD NOT FIND THE FILE 'source.txt'")
        return []

def display_source():
    try:
        with open('source.txt', 'r') as file:
            source=file.readlines()
            source=[s.strip() for s in source]
            for i in range(len(source)):
                print(f"\t\t{i+1} : {source[i]}")
    except FileNotFoundError:
        print("ERROR : COULD NOT FIND THE FILE 'source.txt'")
        return []


def add_source():
    source=input("\n\t\tENTER THE SOURCE : ")
    with open('source.txt', 'a') as file:
        file.write('\n')
        file.write(source)
    print("!!!! SOURCE ADDED SUCCESSFULLY !!!!\n")

def source_menu():
    while True:
        print(f'''
            SOURCE MENU
            -------------
            1. ADD SOURCE
            2. DISPLAY SOURCE
            3. GO BACK
                ''')
        choice=input("\t\tENTER CHOICE : ")
        if choice=='1':
            add_source()
        elif choice=='2':
            display_source()
        else:
            print("\n... GOING BACK ...")
            break