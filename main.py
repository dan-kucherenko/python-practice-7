from app.io.output import print_to_console, write_to_file
from app.io.input import get_user_input, read_input_file, read_input_file_pandas


def main():
    # Read user input
    user_input = get_user_input()

    # Print user input to console
    print_to_console(user_input)
    # Write user input to file
    write_to_file("data/user_input.txt", user_input)

    # Read data from the "input.txt" file
    file_lines = read_input_file("data/input.txt")

    # Print read data to console
    for line in file_lines:
        print_to_console(line.strip())
    # Write read data to file
    write_to_file("data/input_output.txt", ''.join(file_lines))

    # Read data from the "input.csv" file using pandas
    dataframe = read_input_file_pandas("data/input.csv")

    # Print read data to console
    print_to_console(dataframe)
    # Write read data to file in CSV format
    dataframe.to_csv("data/input_output.csv", index=False)


if __name__ == "__main__":
    main()
