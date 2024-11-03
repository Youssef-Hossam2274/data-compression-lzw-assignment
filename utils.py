def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None


def read_file_by_line(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None


def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"Content written to {file_path}")
