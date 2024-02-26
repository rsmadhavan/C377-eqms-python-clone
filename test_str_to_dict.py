def str_to_dict(string):
    stripped_string = string.strip('{}')
 
    pairs = stripped_string.split(', ')
 
    temp_dict = {key[1:-1]: value[1:-1] for key, value in (pair.split(': ') for pair in pairs)}
    # temp_dict['Product Enquired']=temp_dict['Product Enquired'].strip("' }")
    print(temp_dict['Product Enquired'],type(temp_dict),'\n')
    return temp_dict

def read_data():
    with open('enquiry.txt','r') as file:
        data=file.readlines()
        list_dict=[]

        for line in data:
#            printProduct Enquired(line)
            temp_dict=str_to_dict(line)
            list_dict.append(temp_dict)
        print('\n\n')
        print(list_dict)
        # print(str_to_dict(data[0]))

read_data()