from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List, Union
import json


def write_data(data: Dict[str, Any], base_path: str = "data/Users") -> None:
    base_path = Path(base_path)
    base_path.mkdir(parents=True, exist_ok=True)

    file_path = base_path / f"{data['id']}.json"
    s1 = json.dumps(data, default=serialize_datetime, indent=4)
    with file_path.open('w') as file_handle:
        file_handle.write(s1)


def read_data(id: str, base_path: str = "data/Users") -> Dict[str, Any]:
    base_path = Path(base_path)
    file_path = base_path / f"{id}.json"

    if not file_path.exists():
        raise FileNotFoundError(f"User file {file_path} not found.")

    with file_path.open('r') as file_handle:
        data = json.load(file_handle, object_hook=deserialize_datetime)
    return data


def read_list(path: Union[str, Path]) -> List[str]:
    path = Path(path)
    with path.open('r') as file_handle:
        data = file_handle.readlines()
    return data


def serialize_datetime(obj: Any) -> str:
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")


def deserialize_datetime(obj: Dict[str, Any]) -> Dict[str, Any]:
    for key, value in obj.items():
        if isinstance(value, str):
            try:
                obj[key] = datetime.fromisoformat(value)
            except ValueError:
                pass
    return obj


def remove_data(id: str, base_path: str = "data/Users") -> None:
    base_path = Path(base_path)
    valid_paths = {"data/Users", "data/Trains", "data/Routes_files", "data/Carriages"}

    if str(base_path) not in valid_paths:
        raise ValueError(f"Invalid base_path: {base_path}. Allowed paths are: {valid_paths}")

    file_path = base_path / f"{id}.json"

    if file_path.exists():
        file_path.unlink()  # Remove the file
    else:
        raise FileNotFoundError(f"File {file_path} not found.")


def remove_folder(base_path: str = "data/Users") -> None:
    base_path = Path(base_path)
    valid_paths = {"data/Users", "data/Trains", "data/Routes_files", "data/Carriages"}

    if str(base_path) not in valid_paths:
        raise ValueError(f"Invalid base_path: {base_path}. Allowed paths are: {valid_paths}")

    if base_path.exists() and base_path.is_dir():
        for item in base_path.iterdir():
            if item.is_file():
                item.unlink()
    else:
        raise FileNotFoundError(f"Directory {base_path} not found.")
