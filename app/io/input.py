import pandas as pd


def get_user_input():
    return input("Enter user's input:")


def read_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    return lines


def read_input_file_panda(filename):
    dataframe = pd.read_csv(filename)
    return dataframe
