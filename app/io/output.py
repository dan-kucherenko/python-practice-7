def print_to_console(text):
    """
    Print the provided text to the console.

    Args:
        text (str): The text to be printed to the console.
    """
    print(text)


def write_to_file(filename, text):
    """
    Write the provided text to the specified file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to be written to the file.
    """
    try:
        with open(filename, 'w') as file:
            file.write(text)
    except FileNotFoundError:
        print(f'Error writing to file {filename}')
