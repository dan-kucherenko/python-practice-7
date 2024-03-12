import pandas as pd
from app.io.input import read_input_file, read_input_file_pandas


# Test cases for read_input_file
def test_read_input_file_file_exists(tmp_path):
    # Create a temporary file with content
    file_content = "Line 1\nLine 2\nLine 3"
    file_path = tmp_path / "test_input.txt"
    file_path.write_text(file_content)

    # Test reading from the temporary file
    assert read_input_file(file_path) == ["Line 1\n", "Line 2\n", "Line 3"]


def test_read_input_file_file_not_found(tmp_path):
    # Test reading from a non-existent file
    file_path = tmp_path / "non_existent_file.txt"
    assert read_input_file(file_path) == "File not found"


def test_read_input_file_empty_file(tmp_path):
    # Create an empty temporary file
    file_path = tmp_path / "empty_file.txt"
    file_path.touch()

    # Test reading from the empty file
    assert read_input_file(file_path) == []


# Test cases for read_input_file_pandas
def test_read_input_file_pandas_file_exists(tmp_path):
    # Create a temporary CSV file with content
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    csv_path = tmp_path / "test_input.csv"
    df.to_csv(csv_path, index=False)

    # Test reading from the temporary CSV file
    assert read_input_file_pandas(csv_path).equals(df)


def test_read_input_file_pandas_file_not_found(tmp_path):
    # Test reading from a non-existent CSV file
    csv_path = tmp_path / "non_existent_file.csv"
    assert read_input_file_pandas(csv_path) is None


def test_read_input_file_pandas_empty_file(tmp_path):
    # Create an empty temporary CSV file
    csv_path = tmp_path / "empty_file.csv"
    csv_path.touch()

    assert read_input_file_pandas(csv_path) is None
