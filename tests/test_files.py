import pytest
import json
from file_handle.file_handle import write_data, read_data


def get_test_data():
    return {
        "id": "123",
        "data": "abc"
    }


def test_write_data(tmpdir):
    data = get_test_data()
    test_path = tmpdir.mkdir("data").mkdir("Users")
    write_data(data, base_path=str(test_path))
    file_path = test_path / f"{data['id']}.json"
    assert file_path.exists()
    with open(file_path, 'r') as f:
        loaded_data = json.load(f)
        assert loaded_data == data


def test_read_data(tmpdir):
    data = get_test_data()
    test_path = tmpdir.mkdir("data").mkdir("Users")
    write_data(data, base_path=str(test_path))
    loaded_data = read_data(data['id'], base_path=str(test_path))
    assert loaded_data == data


def test_read_data_file_not_found(tmpdir):
    test_path = tmpdir.mkdir("data").mkdir("Users")
    with pytest.raises(FileNotFoundError):
        read_data("nonexistent_id", base_path=str(test_path))
