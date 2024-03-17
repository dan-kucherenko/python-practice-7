import pytest
import pandas as pd
from app.io.input import read_input_file, read_input_file_pandas


@pytest.fixture
def tmp_text_file(tmp_path):
    file_content = "Line 1\nLine 2\nLine 3"
    file_path = tmp_path / "test_input.txt"
    file_path.write_text(file_content)
    return file_path


@pytest.fixture
def tmp_csv_file(tmp_path):
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    csv_path = tmp_path / "test_input.csv"
    df.to_csv(csv_path, index=False)
    return csv_path


def test_read_input_file_file_exists(tmp_text_file):
    assert read_input_file(tmp_text_file) == ["Line 1\n", "Line 2\n", "Line 3"]


def test_read_input_file_file_not_found(tmp_path):
    file_path = tmp_path / "non_existent_file.txt"
    assert read_input_file(file_path) == "File not found"


def test_read_input_file_empty_file(tmp_path):
    file_path = tmp_path / "empty_file.txt"
    file_path.touch()
    assert read_input_file(file_path) == []


def test_read_input_file_pandas_file_exists(tmp_csv_file):
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    assert read_input_file_pandas(tmp_csv_file).equals(df)


def test_read_input_file_pandas_file_not_found(tmp_path):
    csv_path = tmp_path / "non_existent_file.csv"
    assert read_input_file_pandas(csv_path) is None


def test_read_input_file_pandas_empty_file(tmp_path):
    csv_path = tmp_path / "empty_file.csv"
    csv_path.touch()
    assert read_input_file_pandas(csv_path) is None
