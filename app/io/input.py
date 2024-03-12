import pandas as pd


def get_user_input():
    """
    Prompt the user to enter input and return the input entered by the user.

    Returns:
        str: The input entered by the user.
    """
    return input("Enter user's input: ")


def read_input_file(filename):
    """
    Read lines from a file and return them as a list of strings.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        list: A list of strings representing the lines read from the file.
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        return "File not found"


def read_input_file_pandas(filename):
    """
    Read a file using pandas and return the contents as a DataFrame.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        pandas.DataFrame or None: A DataFrame containing the contents of the file,
                                  or None if the file is not found.
    """
    try:
        dataframe = pd.read_csv(filename)
        return dataframe
    except FileNotFoundError:
        print(f'CSV file with path {filename} can\'t be found')
        return None
    except pd.errors.EmptyDataError:
        print(f'CSV file with path {filename} is empty')
        return None
