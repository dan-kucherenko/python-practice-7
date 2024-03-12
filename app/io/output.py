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


def write_dataframe_to_csv(filename, dataframe):
    """
    Write a pandas DataFrame to a CSV file using default Python methods.

    Args:
        filename (str): The name of the file to write to.
        dataframe (pandas.DataFrame): The DataFrame to be written to the file.
    """
    # Open the file for writing
    with open(filename, 'w', newline='') as file:
        # Get column names and write them to the file
        column_names = dataframe.columns.tolist()
        file.write(','.join(column_names) + '\n')

        # Iterate over DataFrame rows and write them to the file
        for index, row in dataframe.iterrows():
            file.write(','.join(map(str, row)) + '\n')
