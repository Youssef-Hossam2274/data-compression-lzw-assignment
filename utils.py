def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None


def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


def get_string_asci_dictionary(): 
    dictionary = {}
    for asci_number in range(128): 
        dictionary[chr(asci_number)] = asci_number
    
    return dictionary

def get_asci_string_dictionary(): 
    dictionary = {}
    for asci_number in range(128): 
        dictionary[asci_number] = chr(asci_number)
    
    return dictionary
