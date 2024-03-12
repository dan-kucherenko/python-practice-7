def print_to_console(text):
    print(text)


def write_to_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)
