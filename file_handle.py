from pathlib import Path
from datetime import datetime
import json


def write_data(data, base_path="data/Users"):
    base_path = Path(base_path)
    base_path.mkdir(parents=True, exist_ok=True)

    file_path = base_path / f"{data.id}.json"
    data = data.json_repr()
    s1 = json.dumps(data, default=serialize_datetime, indent=4)
    with file_path.open('w') as file_handle:
        file_handle.write(s1)


def read_data(id: str, base_path="data/Users"):
    base_path = Path(base_path)
    file_path = base_path / f"{id}.json"

    if not file_path.exists():
        raise FileNotFoundError(f"User file {file_path} not found.")

    with file_path.open('r') as file_handle:
        data = json.load(file_handle, object_hook=deserialize_datetime)
    return data


def read_list(path):
    path = Path(path)
    with path.open('r') as file_handle:
        data = json.load(file_handle)
    return data


def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")


def deserialize_datetime(obj):
    for key, value in obj.items():
        if isinstance(value, str):
            try:
                obj[key] = datetime.fromisoformat(value)
            except ValueError:
                pass
    return obj
