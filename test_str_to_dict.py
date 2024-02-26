def str_to_dict(string):
    # Strip extra '{' and '}' from the beginning and end of the string
    stripped_string = string.strip('{}\n')

    # Split pairs by comma-space and handle cases where there are extra single quotes
    pairs = stripped_string.split(', ')

    # Construct dictionary by splitting each pair by colon-space and stripping any extra characters
    result_dict = {}
    for pair in pairs:
        key, value = pair.split(': ')
        key = key.strip("'")
        value = value.strip("'")
        result_dict[key] = value

    return result_dict

def read_data():
    with open('enquiry.txt', 'r') as file:
        data = file.readlines()
        list_dict = []

        for line in data:
            temp_dict = str_to_dict(line)
            list_dict.append(temp_dict)

    return list_dict

def display_enquiries():
    enquiries = read_data()
    print("Enquiry Number\tCustomer Name\tDate\tContact Person\tAddress\tPhone Number\tEmail\tSource\tProduct Enquired")
    for enquiry in enquiries:
        row = '\t'.join([enquiry[key] for key in enquiry])
        print(row)

display_enquiries()
