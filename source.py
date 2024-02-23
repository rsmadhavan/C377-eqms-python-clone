def get_source():
    with open('source.txt', 'r') as file:
        source=file.readlines()
        source=[s.strip() for s in source]
        return source

def display_source():
    with open('source.txt', 'r') as file:
        source=file.readlines()
        source=[s.strip() for s in source]
        for i in range(len(source)):
            print(f"{i+1} : {source[i]}")

def add_source():
    source=input("Enter the source : ")
    with open('source.txt', 'a') as file:
        file.write('\n')
        file.write(source)
